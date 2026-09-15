#!/usr/bin/env python3
"""
export-coleccion-a-app.py — puente entre data/coleccion.db (skill) y la app web.

La app (index.html/js/app.js) guarda todo en localStorage con su propio
formato de registro (id, type, artist, album, label, year, format, notes,
owner). Este script lee coleccion.db y arma esos registros en el formato
de la app, en dos modalidades:

- `--format json`: para importar a mano con el botón "Importar" de la app.
- `--format js` (default): genera `js/seed-data.js`, que la app carga
  directo al abrir `index.html` y precarga en localStorage si todavía no
  hay nada guardado — sin tocar ningún botón. Correr este script después
  de cada cambio en coleccion.db y commitear el seed-data.js resultante
  para que quede al día.

Uso:
    python3 scripts/export-coleccion-a-app.py                       # regenera js/seed-data.js
    python3 scripts/export-coleccion-a-app.py --format json -o deadwax-import.json

Reglas de conversión:
- status=owned          -> type=collection
- status=pendiente      -> type=wantlist
- status=evaluado_no_comprado -> se omite (no hay bucket equivalente en la
  app: es un disco que se decidió no comprar, no algo pendiente de comprar).
- owner=ana -> "yo", owner=seba -> "seba" (la app usa "yo"/"seba").
- país, catálogo, prensado_notas, grading y matrix no tienen campo propio en
  la app: se empaquetan dentro de "notes" para no perder la info.
"""
import argparse
import json
import os
import sqlite3
import sys

REPO_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DB_PATH = os.path.join(REPO_ROOT, ".claude", "skills", "dead-wax", "data", "coleccion.db")
DEFAULT_JS_OUT = os.path.join(REPO_ROOT, "js", "seed-data.js")

OWNER_MAP = {"ana": "yo", "seba": "seba"}
STATUS_TO_TYPE = {"owned": "collection", "pendiente": "wantlist"}


def build_notes(row):
    parts = []
    if row["pais"]:
        parts.append(f"País: {row['pais']}")
    if row["catalogo"]:
        parts.append(f"Catálogo: {row['catalogo']}")
    grading = " / ".join(g for g in (row["grading_disco"], row["grading_tapa"]) if g)
    if grading:
        parts.append(f"Grading: {grading}")
    if row["prensado_notas"]:
        parts.append(f"Prensado: {row['prensado_notas']}")
    if row["dead_wax_matrix"]:
        parts.append(f"Matrix: {row['dead_wax_matrix']}")
    header = " · ".join(parts)
    if row["notas"]:
        return f"{header}\n{row['notas']}" if header else row["notas"]
    return header


def convert(db_path):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    records, skipped = [], 0
    for row in conn.execute("SELECT * FROM discos"):
        record_type = STATUS_TO_TYPE.get(row["status"])
        if record_type is None:
            skipped += 1
            continue
        record = {
            "id": f"dw-{row['id']}",
            "type": record_type,
            "artist": row["artista"],
            "album": row["titulo"],
            "label": row["sello"] or "",
            "year": str(row["anio"]) if row["anio"] else "",
            "format": "LP",
            "notes": build_notes(row),
        }
        if record_type == "collection":
            record["owner"] = OWNER_MAP.get(row["owner"], "yo")
        records.append(record)
    return records, skipped


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", default=DB_PATH, help="ruta a coleccion.db")
    parser.add_argument(
        "--format", choices=["json", "js"], default="js",
        help="js (default): genera js/seed-data.js para autocarga; json: para importar a mano",
    )
    parser.add_argument(
        "-o", "--out",
        help="archivo de salida (default: js/seed-data.js para --format js, stdout para json)",
    )
    args = parser.parse_args()

    records, skipped = convert(args.db)
    payload = json.dumps(records, ensure_ascii=False, indent=2)

    if args.format == "js":
        out_path = args.out or DEFAULT_JS_OUT
        js_content = (
            "// Generado por scripts/export-coleccion-a-app.py — no editar a mano.\n"
            "// Precarga la colección/wantlist desde coleccion.db la primera vez que se\n"
            "// abre la app (ver seedIfNeeded() en app.js).\n"
            f"window.DEADWAX_SEED = {payload};\n"
        )
        with open(out_path, "w") as f:
            f.write(js_content)
        print(f"Exportados {len(records)} discos a {out_path}", file=sys.stderr)
    elif args.out:
        with open(args.out, "w") as f:
            f.write(payload)
        print(f"Exportados {len(records)} discos a {args.out}", file=sys.stderr)
    else:
        print(payload)

    if skipped:
        print(
            f"Omitidos {skipped} registros con status=evaluado_no_comprado "
            "(no hay bucket equivalente en la app).",
            file=sys.stderr,
        )


if __name__ == "__main__":
    main()

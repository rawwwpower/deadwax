#!/usr/bin/env python3
"""
export-coleccion-a-app.py — puente entre data/coleccion.db (skill) y la app web.

La app (index.html/js/app.js) guarda todo en localStorage con su propio
formato de registro (id, type, artist, album, label, year, format, notes,
owner). Este script lee coleccion.db y arma un JSON en ese formato,
importable con el botón "Importar" de la app.

Uso:
    python3 scripts/export-coleccion-a-app.py > deadwax-import.json
    python3 scripts/export-coleccion-a-app.py -o deadwax-import.json

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

DB_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", ".claude", "skills", "dead-wax", "data", "coleccion.db",
)

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
    parser.add_argument("-o", "--out", help="archivo de salida (default: stdout)")
    args = parser.parse_args()

    records, skipped = convert(args.db)
    output = json.dumps(records, ensure_ascii=False, indent=2)

    if args.out:
        with open(args.out, "w") as f:
            f.write(output)
        print(f"Exportados {len(records)} discos a {args.out}", file=sys.stderr)
    else:
        print(output)

    if skipped:
        print(
            f"Omitidos {skipped} registros con status=evaluado_no_comprado "
            "(no hay bucket equivalente en la app).",
            file=sys.stderr,
        )


if __name__ == "__main__":
    main()

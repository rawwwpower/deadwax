#!/usr/bin/env python3
"""
coleccion.py — CLI para manejar la base de datos local de Dead Wax.

Uso:
    python coleccion.py init
    python coleccion.py add --artista "..." --titulo "..." [opciones]
    python coleccion.py search "texto libre (artista, título o catálogo)"
    python coleccion.py list [--status owned|evaluado_no_comprado|pendiente]
    python coleccion.py show <id>
    python coleccion.py update <id> --status owned [otras opciones]
    python coleccion.py update <id> --review "reseña personal de escucha"
    python coleccion.py delete <id>
    python coleccion.py versiones <id>
    python coleccion.py version-add <id> --orden 1 --edicion "..." [--sonido ... --marca buscar|evitar]
    python coleccion.py stats

La base vive en data/coleccion.db (SQLite), relativa a este script.
No depende de librerías externas, solo sqlite3 de la stdlib.
"""
import argparse
import sqlite3
import os
import sys

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "coleccion.db")

SCHEMA = """
CREATE TABLE IF NOT EXISTS discos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    owner TEXT NOT NULL DEFAULT 'ana',  -- ana | seba
    artista TEXT NOT NULL,
    titulo TEXT NOT NULL,
    pais TEXT,
    sello TEXT,
    catalogo TEXT,
    anio INTEGER,
    genero TEXT,                -- género/subgénero específico, ej. "jazz fusion"
    prensado_notas TEXT,        -- ej. "primera prensa confirmada por PORKY/PECKO"
    dead_wax_matrix TEXT,
    grading_disco TEXT,         -- M / NM / VG+ / VG / G / P
    grading_tapa TEXT,
    status TEXT NOT NULL DEFAULT 'pendiente',  -- owned | evaluado_no_comprado | pendiente | descubrimiento
    discogs_release_id TEXT,
    precio TEXT,
    fecha_adquirido TEXT,
    notas TEXT,
    review TEXT,                -- reseña personal de escucha (sonido, impresiones)
    prioridad TEXT,             -- wishlist: iconico | top | interesante | evitar (secciones de la página)
    etiquetas TEXT,             -- marcas cortas separadas por coma, ej. "país de origen, falta el single"
    resumen TEXT,               -- una línea para la página de vinilos (por qué está, cómo suena)
    fuente TEXT,                -- de dónde salió, ej. "feria 2026-09", "javierfan"
    origen TEXT,                -- país de origen del disco (banda/sello original), criterio 2
    creado_en TEXT DEFAULT CURRENT_TIMESTAMP
);

-- Ranking de ediciones de un disco icónico (una fila por versión, orden 1 = la mejor).
CREATE TABLE IF NOT EXISTS versiones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    disco_id INTEGER NOT NULL REFERENCES discos(id) ON DELETE CASCADE,
    orden INTEGER NOT NULL,
    edicion TEXT NOT NULL,      -- ej. "UK Vertigo swirl 1970"
    catalogo TEXT,
    sonido TEXT,                -- cómo suena, según reviews
    precio TEXT,                -- referencia de precio (texto libre)
    donde TEXT,                 -- dónde se vio, ej. "London Records $130.000"
    marca TEXT,                 -- buscar (la recomendada) | evitar | NULL
    pais TEXT,                  -- país de prensado de esa edición
    confirmar TEXT              -- cómo reconocerla: etiqueta, matrix, tapa, inserts
);
"""

# Columnas agregadas después de la creación inicial de la tabla — migración liviana en get_conn().
MIGRATIONS = [
    ("genero", "TEXT"),
    ("review", "TEXT"),
    ("prioridad", "TEXT"),
    ("etiquetas", "TEXT"),
    ("resumen", "TEXT"),
    ("fuente", "TEXT"),
    ("origen", "TEXT"),
]

# Columnas agregadas a versiones después de crearla.
MIGRATIONS_VERSIONES = [
    ("pais", "TEXT"),
    ("confirmar", "TEXT"),
]

FIELDS = [
    "owner", "artista", "titulo", "pais", "sello", "catalogo", "anio", "genero",
    "prensado_notas", "dead_wax_matrix", "grading_disco", "grading_tapa",
    "status", "discogs_release_id", "precio", "fecha_adquirido", "notas",
    "review", "prioridad", "etiquetas", "resumen", "fuente", "origen",
]


def get_conn():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA)
    existing_cols = {row[1] for row in conn.execute("PRAGMA table_info(discos)")}
    for col, coltype in MIGRATIONS:
        if col not in existing_cols:
            conn.execute(f"ALTER TABLE discos ADD COLUMN {col} {coltype}")
    existing_v = {row[1] for row in conn.execute("PRAGMA table_info(versiones)")}
    for col, coltype in MIGRATIONS_VERSIONES:
        if col not in existing_v:
            conn.execute(f"ALTER TABLE versiones ADD COLUMN {col} {coltype}")
    conn.commit()
    return conn


def cmd_init(args):
    get_conn()
    print(f"Base inicializada en {DB_PATH}")


def cmd_add(args):
    conn = get_conn()
    values = {f: getattr(args, f, None) for f in FIELDS}
    cols = ", ".join(values.keys())
    placeholders = ", ".join(["?"] * len(values))
    conn.execute(
        f"INSERT INTO discos ({cols}) VALUES ({placeholders})",
        list(values.values()),
    )
    conn.commit()
    new_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
    print(f"Agregado con id {new_id}: {args.artista} — {args.titulo}")


def _print_rows(rows):
    if not rows:
        print("(sin resultados)")
        return
    for r in rows:
        genero = r['genero'] if 'genero' in r.keys() else None
        print(f"[{r['id']}] ({r['owner']}) {r['artista']} — {r['titulo']} "
              f"({r['pais'] or '?'}, {r['sello'] or '?'}, cat. {r['catalogo'] or '?'}, {r['anio'] or '?'}) "
              f"[{r['status']}] {genero or '?'} {r['grading_disco'] or ''}/{r['grading_tapa'] or ''}")


def cmd_search(args):
    conn = get_conn()
    q = f"%{args.texto}%"
    rows = conn.execute(
        "SELECT * FROM discos WHERE artista LIKE ? OR titulo LIKE ? OR catalogo LIKE ? OR sello LIKE ? "
        "OR genero LIKE ? OR pais LIKE ?",
        [q] * 6,
    ).fetchall()
    _print_rows(rows)


def cmd_list(args):
    conn = get_conn()
    clauses, params = [], []
    if args.status:
        clauses.append("status = ?")
        params.append(args.status)
    if args.owner:
        clauses.append("owner = ?")
        params.append(args.owner)
    if args.incomplete:
        clauses.append(
            "(pais IS NULL OR pais = '' OR sello IS NULL OR sello = '' "
            "OR catalogo IS NULL OR catalogo = '')"
        )
    where = f"WHERE {' AND '.join(clauses)}" if clauses else ""
    rows = conn.execute(f"SELECT * FROM discos {where} ORDER BY artista", params).fetchall()
    _print_rows(rows)


def cmd_show(args):
    conn = get_conn()
    r = conn.execute("SELECT * FROM discos WHERE id = ?", [args.id]).fetchone()
    if not r:
        print("No existe ese id.")
        return
    for k in r.keys():
        print(f"{k}: {r[k]}")


def cmd_update(args):
    conn = get_conn()
    updates = {f: getattr(args, f) for f in FIELDS if getattr(args, f, None) is not None}
    if not updates:
        print("Nada para actualizar.")
        return
    set_clause = ", ".join(f"{k} = ?" for k in updates)
    conn.execute(f"UPDATE discos SET {set_clause} WHERE id = ?", list(updates.values()) + [args.id])
    conn.commit()
    print(f"Actualizado id {args.id}.")


def cmd_delete(args):
    conn = get_conn()
    r = conn.execute("SELECT artista, titulo FROM discos WHERE id = ?", [args.id]).fetchone()
    if not r:
        print("No existe ese id.")
        return
    conn.execute("DELETE FROM discos WHERE id = ?", [args.id])
    conn.commit()
    print(f"Borrado id {args.id}: {r['artista']} — {r['titulo']}")


def cmd_versiones(args):
    conn = get_conn()
    rows = conn.execute("SELECT * FROM versiones WHERE disco_id = ? ORDER BY orden", [args.disco_id]).fetchall()
    if not rows:
        print("(sin versiones)")
    for r in rows:
        marca = f" [{r['marca']}]" if r['marca'] else ""
        print(f"{r['orden']}. {r['edicion']} ({r['catalogo'] or '?'}){marca} — {r['sonido'] or ''} | {r['precio'] or ''} | {r['donde'] or ''}")


def cmd_version_add(args):
    conn = get_conn()
    conn.execute(
        "INSERT INTO versiones (disco_id, orden, edicion, catalogo, sonido, precio, donde, marca, pais, confirmar) "
        "VALUES (?,?,?,?,?,?,?,?,?,?)",
        [args.disco_id, args.orden, args.edicion, args.catalogo, args.sonido, args.precio, args.donde, args.marca,
         args.pais, args.confirmar],
    )
    conn.commit()
    print(f"Versión {args.orden} agregada al disco {args.disco_id}.")


def cmd_stats(args):
    conn = get_conn()
    total = conn.execute("SELECT COUNT(*) FROM discos").fetchone()[0]
    print(f"Total de registros: {total}")
    for row in conn.execute("SELECT status, COUNT(*) as n FROM discos GROUP BY status"):
        print(f"  {row['status']}: {row['n']}")


def build_parser():
    p = argparse.ArgumentParser(description="CLI de la colección Dead Wax")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("init").set_defaults(func=cmd_init)

    add_p = sub.add_parser("add")
    add_p.add_argument("--owner", default="ana", choices=["ana", "seba"])
    add_p.add_argument("--artista", required=True)
    add_p.add_argument("--titulo", required=True)
    add_p.add_argument("--pais")
    add_p.add_argument("--sello")
    add_p.add_argument("--catalogo")
    add_p.add_argument("--anio", type=int)
    add_p.add_argument("--genero")
    add_p.add_argument("--prensado-notas", dest="prensado_notas")
    add_p.add_argument("--dead-wax-matrix", dest="dead_wax_matrix")
    add_p.add_argument("--grading-disco", dest="grading_disco")
    add_p.add_argument("--grading-tapa", dest="grading_tapa")
    add_p.add_argument("--status", default="pendiente",
                        choices=["owned", "evaluado_no_comprado", "pendiente", "descubrimiento"])
    add_p.add_argument("--discogs-release-id", dest="discogs_release_id")
    add_p.add_argument("--precio")
    add_p.add_argument("--fecha-adquirido", dest="fecha_adquirido")
    add_p.add_argument("--notas")
    add_p.add_argument("--review")
    add_p.add_argument("--prioridad", choices=["iconico", "top", "interesante", "evitar"])
    add_p.add_argument("--etiquetas")
    add_p.add_argument("--resumen")
    add_p.add_argument("--fuente")
    add_p.add_argument("--origen", help="país de origen del disco (banda/sello original)")
    add_p.set_defaults(func=cmd_add)

    search_p = sub.add_parser("search")
    search_p.add_argument("texto")
    search_p.set_defaults(func=cmd_search)

    list_p = sub.add_parser("list")
    list_p.add_argument("--status", choices=["owned", "evaluado_no_comprado", "pendiente", "descubrimiento"])
    list_p.add_argument("--owner", choices=["ana", "seba"])
    list_p.add_argument(
        "--incomplete", action="store_true",
        help="solo discos con país, sello o catálogo vacío (para rondas de repaso)",
    )
    list_p.set_defaults(func=cmd_list)

    show_p = sub.add_parser("show")
    show_p.add_argument("id", type=int)
    show_p.set_defaults(func=cmd_show)

    update_p = sub.add_parser("update")
    update_p.add_argument("id", type=int)
    for f in FIELDS:
        update_p.add_argument(f"--{f.replace('_', '-')}", dest=f)
    update_p.set_defaults(func=cmd_update)

    delete_p = sub.add_parser("delete", help="borrar un registro (ej. un duplicado ya fusionado)")
    delete_p.add_argument("id", type=int)
    delete_p.set_defaults(func=cmd_delete)

    ver_p = sub.add_parser("versiones", help="ranking de ediciones de un disco icónico")
    ver_p.add_argument("disco_id", type=int)
    ver_p.set_defaults(func=cmd_versiones)

    va_p = sub.add_parser("version-add", help="sumar una edición al ranking de un disco icónico")
    va_p.add_argument("disco_id", type=int)
    va_p.add_argument("--orden", type=int, required=True)
    va_p.add_argument("--edicion", required=True)
    va_p.add_argument("--catalogo")
    va_p.add_argument("--sonido")
    va_p.add_argument("--precio")
    va_p.add_argument("--donde")
    va_p.add_argument("--marca", choices=["buscar", "evitar"])
    va_p.add_argument("--pais")
    va_p.add_argument("--confirmar", help="cómo reconocerla: etiqueta, matrix, tapa, inserts")
    va_p.set_defaults(func=cmd_version_add)

    sub.add_parser("stats").set_defaults(func=cmd_stats)

    return p


if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)

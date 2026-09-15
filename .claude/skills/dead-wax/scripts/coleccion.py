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
    prensado_notas TEXT,        -- ej. "primera prensa confirmada por PORKY/PECKO"
    dead_wax_matrix TEXT,
    grading_disco TEXT,         -- M / NM / VG+ / VG / G / P
    grading_tapa TEXT,
    status TEXT NOT NULL DEFAULT 'pendiente',  -- owned | evaluado_no_comprado | pendiente
    discogs_release_id TEXT,
    precio TEXT,
    fecha_adquirido TEXT,
    notas TEXT,
    creado_en TEXT DEFAULT CURRENT_TIMESTAMP
);
"""

FIELDS = [
    "owner", "artista", "titulo", "pais", "sello", "catalogo", "anio",
    "prensado_notas", "dead_wax_matrix", "grading_disco", "grading_tapa",
    "status", "discogs_release_id", "precio", "fecha_adquirido", "notas",
]


def get_conn():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def cmd_init(args):
    conn = get_conn()
    conn.executescript(SCHEMA)
    conn.commit()
    print(f"Base inicializada en {DB_PATH}")


def cmd_add(args):
    conn = get_conn()
    conn.executescript(SCHEMA)
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
        print(f"[{r['id']}] ({r['owner']}) {r['artista']} — {r['titulo']} "
              f"({r['pais'] or '?'}, {r['sello'] or '?'}, cat. {r['catalogo'] or '?'}, {r['anio'] or '?'}) "
              f"[{r['status']}] {r['grading_disco'] or ''}/{r['grading_tapa'] or ''}")


def cmd_search(args):
    conn = get_conn()
    q = f"%{args.texto}%"
    rows = conn.execute(
        "SELECT * FROM discos WHERE artista LIKE ? OR titulo LIKE ? OR catalogo LIKE ? OR sello LIKE ?",
        [q, q, q, q],
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
    add_p.add_argument("--prensado-notas", dest="prensado_notas")
    add_p.add_argument("--dead-wax-matrix", dest="dead_wax_matrix")
    add_p.add_argument("--grading-disco", dest="grading_disco")
    add_p.add_argument("--grading-tapa", dest="grading_tapa")
    add_p.add_argument("--status", default="pendiente", choices=["owned", "evaluado_no_comprado", "pendiente"])
    add_p.add_argument("--discogs-release-id", dest="discogs_release_id")
    add_p.add_argument("--precio")
    add_p.add_argument("--fecha-adquirido", dest="fecha_adquirido")
    add_p.add_argument("--notas")
    add_p.set_defaults(func=cmd_add)

    search_p = sub.add_parser("search")
    search_p.add_argument("texto")
    search_p.set_defaults(func=cmd_search)

    list_p = sub.add_parser("list")
    list_p.add_argument("--status", choices=["owned", "evaluado_no_comprado", "pendiente"])
    list_p.add_argument("--owner", choices=["ana", "seba"])
    list_p.set_defaults(func=cmd_list)

    show_p = sub.add_parser("show")
    show_p.add_argument("id", type=int)
    show_p.set_defaults(func=cmd_show)

    update_p = sub.add_parser("update")
    update_p.add_argument("id", type=int)
    for f in FIELDS:
        update_p.add_argument(f"--{f.replace('_', '-')}", dest=f)
    update_p.set_defaults(func=cmd_update)

    sub.add_parser("stats").set_defaults(func=cmd_stats)

    return p


if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)

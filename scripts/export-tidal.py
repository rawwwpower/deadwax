#!/usr/bin/env python3
"""export-tidal.py — arma dos CSV (Artist,Album) desde coleccion.db para importar en Tidal
con TuneMyMusic o Soundiiz (Tidal no tiene conector directo):

  exports/tidal/coleccion.csv  — discos de Ana (status owned)
  exports/tidal/quiero.csv     — wishlist (pendiente, sin 'evitar') + para escuchar (descubrimiento)

Se saca del título lo que describe la edición ("(12\")", "(vinilo blanco)", etc.) para que el
buscador del servicio encuentre el álbum. Regenerar después de cambios en la base.
"""
import csv, re, sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / ".claude/skills/dead-wax/data/coleccion.db"
OUT = ROOT / "exports/tidal"

def limpiar(t):
    t = re.sub(r"\s*(\([^)]*\)|\[[^]]*\])", "", t or "")
    return re.sub(r"\s+", " ", t).strip()

def dump(nombre, sql):
    db = sqlite3.connect(DB)
    vistos, filas = set(), []
    for art, tit in db.execute(sql):
        fila = (limpiar(art), limpiar(tit))
        if fila[0] and fila[1] and fila not in vistos:
            vistos.add(fila); filas.append(fila)
    filas.sort(key=lambda f: (f[0].lower(), f[1].lower()))
    with open(OUT / nombre, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["Artist", "Album"]); w.writerows(filas)
    print(f"{nombre}: {len(filas)} discos")

OUT.mkdir(parents=True, exist_ok=True)
dump("coleccion.csv", "select artista, titulo from discos where owner='ana' and status='owned'")
dump("quiero.csv", "select artista, titulo from discos where owner='ana' and "
     "((status='pendiente' and coalesce(prioridad,'')<>'evitar') or status='descubrimiento')")

# Genera vinilos.html (la página/artifact "vinilos": colección + wishlist + buscador)
# desde data/coleccion.db, que es la única fuente de verdad. Correr después de cada
# cambio en la base y republicar el artifact con la tool Artifact (mismo url).
#
#   colección = status owned (ana y seba)
#   wishlist  = discos con prioridad iconico | top | interesante que no son owned.
#               Los icónicos salen como ficha, con el ranking de ediciones de la tabla versiones.
#               Los descartados (evitar) no se muestran: una edición a evitar de un icónico va
#               como versión con marca 'evitar' dentro de su ficha.
#
# uso: python3 build.py
import datetime, json, os, re, sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(HERE, '..', '..', 'data', 'coleccion.db')
USD = 1600  # pesos por dólar para la columna de precio

# genero (específico, el de la base) -> estilo (filtro de la página). Gana la primera coincidencia.
ESTILOS = [
    (('banda de sonido',), 'bandas de sonido'),
    (('rock argentino',), 'rock argentino'),
    (('kraut', 'space rock', 'prog'), 'prog / kraut'),
    (('metal', 'hard rock', 'grunge'), 'metal / hard rock'),
    (('punk', 'new wave', 'synth'), 'punk / new wave'),
    (('jazz',), 'jazz'),
    (('electr', 'big beat', 'trip hop', 'rave'), 'electrónica'),
    (('soul', 'funk', 'disco', 'boogie', 'hi-nrg', 'dance'), 'soul / funk / disco'),
    (('mpb',), 'mpb'),
    (('reggae',), 'reggae'),
    (('cantautor',), 'cantautores'),
    (('flamenco',), 'flamenco'),
    (('exotica',), 'exotica'),
    (('rock',), 'rock'),
    (('pop',), 'pop'),
]


def estilo(genero):
    g = (genero or '').lower()
    for keys, name in ESTILOS:
        if any(k in g for k in keys):
            return name
    return 'otros'


def key(r):
    return f"{r['artista']} | {r['titulo']}"


def disc_rows(conn):
    return conn.execute(
        "SELECT * FROM discos WHERE status = 'owned' "
        "OR (prioridad IN ('iconico', 'top', 'interesante') AND status != 'owned') "
        "ORDER BY lower(artista), anio, lower(titulo)"
    ).fetchall()


def precio(v):
    try:
        return int(float(v)) if v not in (None, '') else None
    except ValueError:
        return None


def grading(r):
    d, t = r['grading_disco'], r['grading_tapa']
    # en la base a veces hay aclaraciones entre paréntesis; en la página va solo la nota
    d = re.sub(r'\s*\(.*\)', '', d) if d else None
    t = re.sub(r'\s*\(.*\)', '', t) if t else None
    if d and t:
        return f"{d} / {t}"
    if d:
        return d
    if t:
        return f"tapa {t}"
    return None


def item(r):
    owned = r['status'] == 'owned'
    x = {
        'l': 'coleccion' if owned else 'wishlist',
        'o': r['owner'],
        'p': r['prioridad'],
        'a': r['artista'], 'd': r['titulo'],
        'pa': r['pais'], 'se': r['sello'], 'ca': r['catalogo'], 'y': r['anio'],
        'g': grading(r), 'e': estilo(r['genero']),
        'ed': r['prensado_notas'] if not owned and r['fuente'] == 'feria 2026-09' else None,
        'fl': r['etiquetas'],
        'w': r['resumen'], 'r': re.sub(r'^(Ana|Seba):\s*', '', r['review'] or ''),
        'pr': precio(r['precio']),
        # solo para el buscador, no se muestra
        'n': ' '.join(filter(None, [r['genero'], r['notas'], r['prensado_notas'], r['fuente']])),
    }
    return {k: v for k, v in x.items() if v not in (None, '')}


def versiones(conn, disco_id):
    keys = {'edicion': 'e', 'catalogo': 'c', 'sonido': 's', 'precio': 'p', 'donde': 'w', 'marca': 'm'}
    rows = conn.execute('SELECT * FROM versiones WHERE disco_id = ? ORDER BY orden', [disco_id]).fetchall()
    return [{k: r[col] for col, k in keys.items() if r[col]} for r in rows]


def main():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    rows = disc_rows(conn)
    data = []
    for r in rows:
        x = item(r)
        if r['prioridad'] == 'iconico' and r['status'] != 'owned':
            x['v'] = versiones(conn, r['id'])
        data.append(x)
    covers_all = json.load(open(os.path.join(HERE, 'covers.json')))
    covers = {k: v for k, v in covers_all.items() if k in {key(r) for r in rows}}
    tpl = open(os.path.join(HERE, 'template.html')).read()
    fonts = open(os.path.join(HERE, 'fonts.css')).read()
    out = (tpl.replace('/*FONTS*/', fonts)
              .replace('/*COVERS*/', json.dumps(covers, ensure_ascii=False))
              .replace('/*DATA*/', json.dumps(data, ensure_ascii=False, separators=(',', ':')))
              .replace('/*USD*/', str(USD))
              .replace('/*FECHA*/', datetime.date.today().strftime('%d/%m/%Y')))
    open(os.path.join(HERE, 'vinilos.html'), 'w').write(out)
    n = {l: sum(1 for x in data if x['l'] == l) for l in ('coleccion', 'wishlist')}
    sin_tapa = [key(r) for r in rows if key(r) not in covers]
    print(f"vinilos.html: {n['coleccion']} en colección, {n['wishlist']} en wishlist, "
          f"{len(covers)} tapas, {len(out) // 1024} KB")
    if sin_tapa:
        print(f"sin tapa ({len(sin_tapa)}): " + '; '.join(sin_tapa))


if __name__ == '__main__':
    main()

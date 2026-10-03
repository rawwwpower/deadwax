# Genera nana.html (nana: la webapp con forma de iPod nano) desde data/coleccion.db,
# igual que el artifact "vinilos": la base es la única fuente de verdad, nana.html no
# se edita a mano. Reusa las reglas de vinilos/build.py (colección, wishlist, estilos,
# grading, tapas) y suma los descubrimientos y los samples de media/.
#
#   uso: python3 nana/build.py   (después, republicar nana.html con la tool Artifact)
import base64, datetime, importlib.util, json, os, sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
VINILOS = os.path.join(HERE, '..', '.claude', 'skills', 'dead-wax', 'curaduria', 'vinilos')

spec = importlib.util.spec_from_file_location('vinilos_build', os.path.join(VINILOS, 'build.py'))
vb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vb)


def rows(conn):
    # lo mismo que muestra vinilos, más los descubrimientos (fichas rápidas)
    return conn.execute(
        "SELECT * FROM discos WHERE status IN ('owned', 'descubrimiento') "
        "OR (prioridad IN ('iconico', 'top', 'interesante') AND status != 'owned') "
        "ORDER BY lower(artista), anio, lower(titulo)"
    ).fetchall()


def record(conn, r, cover_idx):
    x = vb.item(r)
    x.pop('n', None)
    if r['status'] == 'descubrimiento':
        x['l'] = 'descubrimiento'
        x.pop('p', None)
    x.update({k: v for k, v in {
        'gen': r['genero'],
        'no': r['notas'],
        'pn': r['prensado_notas'],
        'c': cover_idx.get(vb.key(r)),
    }.items() if v not in (None, '')})
    if r['prioridad'] == 'iconico' and r['status'] != 'owned':
        x['v'] = vb.versiones(conn, r['id'])
    return x


def data_uri(path, mime):
    return f"data:{mime};base64," + base64.b64encode(open(path, 'rb').read()).decode()


def main():
    conn = sqlite3.connect(vb.DB)
    conn.row_factory = sqlite3.Row
    rs = rows(conn)
    covers_all = json.load(open(os.path.join(VINILOS, 'covers.json')))
    keys = [vb.key(r) for r in rs if vb.key(r) in covers_all]
    covers = [covers_all[k] for k in keys]
    cover_idx = {k: i for i, k in enumerate(keys)}
    data = [record(conn, r, cover_idx) for r in rs]
    media = os.path.join(HERE, 'media')
    out = (open(os.path.join(HERE, 'template.html')).read()
           .replace('/*DATA*/', json.dumps(data, ensure_ascii=False, separators=(',', ':')))
           .replace('/*COVERS*/', json.dumps(covers))
           .replace('/*AUDIO*/', data_uri(os.path.join(media, 'dead-wax-2005.mp3'), 'audio/mpeg'))
           .replace('/*VIDEO*/', data_uri(os.path.join(media, 'dead-wax-2005.mp4'), 'video/mp4'))
           .replace('/*FECHA*/', datetime.date.today().strftime('%d/%m/%Y')))
    open(os.path.join(HERE, 'nana.html'), 'w').write(out)
    n = {}
    for x in data:
        n[x['l']] = n.get(x['l'], 0) + 1
    print(f"nana.html: {n}, {len(covers)} tapas, {len(out) // 1024} KB")


if __name__ == '__main__':
    main()

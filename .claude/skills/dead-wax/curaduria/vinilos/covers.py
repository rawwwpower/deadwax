# Baja las tapas (88x88 JPEG embebible) de Cover Art Archive para cada clave de mbids.json
# y las guarda en covers.json. Valor en mbids.json: id de release-group, o "release:<id>" para
# forzar un release puntual cuando la miniatura del grupo no es la tapa (ej. muestra la etiqueta).
# uso: python3 covers.py ["Artista | Título" ...]
#   sin args: baja las tapas que faltan en covers.json; con args: (re)baja solo esas claves
import base64, io, json, os, re, sys, time, urllib.error, urllib.request
from PIL import Image

UA = {'User-Agent': 'DeadWaxCurator/1.0' + (f" ( {os.environ['MB_CONTACT']} )" if os.environ.get('MB_CONTACT') else '')}
HERE = os.path.dirname(os.path.abspath(__file__))


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


nr = urllib.request.build_opener(NoRedirect)


def item_for(mb):
    # CAA redirige a archive.org/download/mbid-<release>/...; los nodos dnXXX/iaXXX.archive.org
    # están bloqueados por el proxy, así que solo nos quedamos con el identificador del item.
    kind, _, mid = mb.partition(':') if mb.startswith('release:') else ('release-group', '', mb)
    try:
        nr.open(urllib.request.Request(f'https://coverartarchive.org/{kind}/{mid}/front-250', headers=UA), timeout=40)
    except urllib.error.HTTPError as e:
        m = re.search(r'/download/(mbid-[0-9a-f-]+)/', e.headers.get('Location', ''))
        if m:
            return m.group(1)
        raise
    raise RuntimeError('sin redirect')


def thumb(item, size=88):
    # archive.org/services/img sirve el __ia_thumb.jpg (~180px, la primera imagen del item) sin redirigir
    raw = urllib.request.urlopen(urllib.request.Request(f'https://archive.org/services/img/{item}', headers=UA), timeout=40).read()
    return Image.open(io.BytesIO(raw)).convert('RGB').resize((size, size), Image.LANCZOS)


def main(only):
    cj = os.path.join(HERE, 'covers.json')
    m = json.load(open(os.path.join(HERE, 'mbids.json')))
    out = json.load(open(cj)) if os.path.exists(cj) else {}
    miss = []
    for k, mb in m.items():
        if only and k not in only:
            continue
        if not only and k in out:
            continue
        if not mb:
            miss.append(k)
            continue
        try:
            b = io.BytesIO()
            thumb(item_for(mb)).save(b, 'JPEG', quality=62, optimize=True, progressive=True)
            out[k] = 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()
            print('ok', k, len(b.getvalue()), flush=True)
        except Exception as e:
            miss.append(k)
            print('MISS', k, str(e)[:80], flush=True)
        time.sleep(0.3)
    json.dump(out, open(cj, 'w'), ensure_ascii=False)
    print('total bytes', sum(len(v) for v in out.values()), 'missing', miss)


if __name__ == '__main__':
    main(sys.argv[1:])

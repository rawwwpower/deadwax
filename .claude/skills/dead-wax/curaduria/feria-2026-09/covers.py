import json,io,base64,urllib.request,urllib.error,time,re
from PIL import Image
import os,sys
UA={'User-Agent':'DeadWaxCurator/1.0' + (f" ( {os.environ['MB_CONTACT']} )" if os.environ.get('MB_CONTACT') else '')}

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,*a,**k): return None
nr=urllib.request.build_opener(NoRedirect)

def item_for(mb):
    # CAA redirige a archive.org/download/mbid-<release>/...; los nodos dnXXX/iaXXX.archive.org
    # están bloqueados por el proxy, así que solo nos quedamos con el identificador del item.
    try:
        nr.open(urllib.request.Request(f'https://coverartarchive.org/release-group/{mb}/front-250',headers=UA),timeout=40)
    except urllib.error.HTTPError as e:
        loc=e.headers.get('Location','')
        m=re.search(r'/download/(mbid-[0-9a-f-]+)/',loc)
        if m: return m.group(1)
        raise
    raise RuntimeError('sin redirect')

# uso: python3 covers.py ["Artista | Título" ...]  -> sin args baja todo; con args reintenta solo esos y los suma a covers.json
here=os.path.dirname(os.path.abspath(__file__)); cj=os.path.join(here,'covers.json')
m=json.load(open(os.path.join(here,'mbids.json'))); only=sys.argv[1:]
out=json.load(open(cj)) if only and os.path.exists(cj) else {}; miss=[]
for k,mb in m.items():
    if only and k not in only: continue
    if not mb: miss.append(k); continue
    try:
        item=item_for(mb)
        # archive.org/services/img sirve el __ia_thumb.jpg (~180px, la tapa frontal) sin redirigir
        raw=urllib.request.urlopen(urllib.request.Request(f'https://archive.org/services/img/{item}',headers=UA),timeout=40).read()
        im=Image.open(io.BytesIO(raw)).convert('RGB')
        im=im.resize((88,88),Image.LANCZOS)
        b=io.BytesIO(); im.save(b,'JPEG',quality=62,optimize=True,progressive=True)
        out[k]='data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
        print('ok',k,len(b.getvalue()),flush=True)
    except Exception as e:
        miss.append(k); print('MISS',k,str(e)[:80],flush=True)
    time.sleep(0.3)
json.dump(out,open(cj,'w'),ensure_ascii=False)
print('total bytes',sum(len(v) for v in out.values()),'missing',miss)

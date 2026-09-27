import json,io,base64,urllib.request,time
from PIL import Image
import os
UA={'User-Agent':'DeadWaxCurator/1.0' + (f" ( {os.environ['MB_CONTACT']} )" if os.environ.get('MB_CONTACT') else '')}
m=json.load(open(os.path.join(os.path.dirname(__file__),'mbids.json'))); out={}; miss=[]
for k,mb in m.items():
    if not mb: miss.append(k); continue
    try:
        raw=urllib.request.urlopen(urllib.request.Request(f'https://coverartarchive.org/release-group/{mb}/front-250',headers=UA),timeout=40).read()
        im=Image.open(io.BytesIO(raw)).convert('RGB'); im.thumbnail((88,88)) if im.size[0]==im.size[1] else None
        im=im.resize((88,88),Image.LANCZOS)
        b=io.BytesIO(); im.save(b,'JPEG',quality=62,optimize=True,progressive=True)
        out[k]='data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
        print('ok',k,len(b.getvalue()),flush=True)
    except Exception as e:
        miss.append(k); print('MISS',k,str(e)[:80],flush=True)
    time.sleep(0.3)
json.dump(out,open(os.path.join(os.path.dirname(__file__),'covers.json'),'w'))
print('total bytes',sum(len(v) for v in out.values()),'missing',miss)

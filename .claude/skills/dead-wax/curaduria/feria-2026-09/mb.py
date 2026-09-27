import json,re,time,urllib.request,urllib.parse
import os
UA={'User-Agent':'DeadWaxCurator/1.0' + (f" ( {os.environ['MB_CONTACT']} )" if os.environ.get('MB_CONTACT') else '')}
src=open(os.path.join(os.path.dirname(__file__),'full_data.js')).read()
items=re.findall(r'a:"([^"]+)",d:"([^"]+)"',src)
Q={ # search overrides
 ("Charlie Haden / Jan Garbarek / Egberto Gismonti","Folk Songs"):("Charlie Haden","Folk Songs"),
 ("Duke Ellington & Count Basie","First Time! The Count Meets the Duke"):("Duke Ellington","First Time! The Count Meets the Duke"),
 ("Mercedes Sosa","Hasta la Victoria · Mujeres Argentinas · Con Sabor a Mercedes Sosa"):("Mercedes Sosa","Mujeres argentinas"),
 ("Keith Jarrett","Invocations / The Moth and the Flame"):("Keith Jarrett","Invocations / The Moth and the Flame"),
 ("Bill Bruford & Patrick Moraz","Music for Piano and Drums"):("Patrick Moraz","Music for Piano and Drums"),
 ("Ian Dury & The Blockheads","Do It Yourself"):("Ian Dury","Do It Yourself"),
 ("Paco de Lucía","Interpreta a Manuel de Falla"):("Paco de Lucía","Interpreta a Manuel de Falla"),
 ("Judas Priest","Priest in the East"):("Judas Priest","Unleashed in the East"),
 ("Queen","Queen I"):("Queen","Queen"),
 ("Talking Heads","Fear of Muzak"):None,("Boston","The Band from the Platinum Basement"):None,
}
out={}
for a,d in dict.fromkeys(items):
    k=f"{a} | {d}"
    q=Q.get((a,d),(a,d))
    if q is None: out[k]=None; continue
    qa,qd=q
    lu=f'releasegroup:"{qd}" AND artist:"{qa}"'
    url='https://musicbrainz.org/ws/2/release-group/?'+urllib.parse.urlencode({'query':lu,'fmt':'json','limit':3})
    for i in range(3):
        try:
            r=json.load(urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=30)); break
        except Exception as e: time.sleep(3); r={}
    rg=r.get('release-groups',[])
    out[k]=rg[0]['id'] if rg else None
    print(k,'->',(rg[0]['title'] if rg else None),flush=True)
    time.sleep(1.2)
json.dump(out,open(os.path.join(os.path.dirname(__file__),'mbids.json'),'w'),ensure_ascii=False,indent=0)

# Busca en MusicBrainz el release-group de cada disco de la página (colección + wishlist)
# y lo guarda en mbids.json, clave "Artista | Título". Solo consulta las claves que faltan.
# uso: python3 mb.py            (MB_CONTACT=<mail alternativo> opcional, nunca el principal)
import json, os, sqlite3, time, urllib.parse, urllib.request
from build import DB, disc_rows, key

HERE = os.path.dirname(os.path.abspath(__file__))
UA = {'User-Agent': 'DeadWaxCurator/1.0' + (f" ( {os.environ['MB_CONTACT']} )" if os.environ.get('MB_CONTACT') else '')}
OUT = os.path.join(HERE, 'mbids.json')

# Búsquedas que necesitan otro artista/título para encontrar el disco; None = no buscar (bootlegs, etc.)
Q = {
    "Charlie Haden / Jan Garbarek / Egberto Gismonti | Folk Songs": ("Charlie Haden", "Folk Songs"),
    "Duke Ellington & Count Basie | First Time! The Count Meets the Duke": ("Duke Ellington", "First Time! The Count Meets the Duke"),
    "Mercedes Sosa | Hasta la Victoria · Mujeres Argentinas · Con Sabor a Mercedes Sosa": ("Mercedes Sosa", "Mujeres argentinas"),
    "Bill Bruford & Patrick Moraz | Music for Piano and Drums": ("Patrick Moraz", "Music for Piano and Drums"),
    "Ian Dury & The Blockheads | Do It Yourself": ("Ian Dury", "Do It Yourself"),
    "Judas Priest | Priest in the East": ("Judas Priest", "Unleashed in the East"),
    "Queen | Queen I": ("Queen", "Queen"),
    "Talking Heads | Fear of Muzak": None,
    "Boston | The Band from the Platinum Basement": None,
    "Various | Breakouts Vol. 5": None,
    "Varios (OST) | Orange Mécanique (A Clockwork Orange)": ("Various Artists", "A Clockwork Orange"),
    "Varios (OST) | Escape From New York": ("John Carpenter", "Escape From New York"),
    "Walter Carlos | Electronic Bach (Switched-On Bach)": ("Walter Carlos", "Switched-On Bach"),
    "Leonardo Favio | Nazareno Cruz y el Lobo (B.S.O.)": ("Leonardo Favio", "Nazareno Cruz y el Lobo"),
    "Mister Sam | From Paris to New York (test pressing)": ("Mister Sam", "From Paris to New York"),
    "Stevie Wonder | Original Musiquarium I": ("Stevie Wonder", "Original Musiquarium I"),
    "Madonna | American Life [álbum, copia promo]": ("Madonna", "American Life"),
    "Madonna | American Life [promo sin identificar: Love Profusion / Nobody Knows Me / Nothing Fails]": ("Madonna", "American Life"),
    "Madonna | American Life (Missy Elliott American Dream Remixes)": ("Madonna", "American Life"),
    "Madonna | Music (single, no el álbum)": ("Madonna", "Music"),
    "The Chemical Brothers | Galvanize (12\")": ("The Chemical Brothers", "Galvanize"),
    "Claudio Simonetti's Goblin | Profondo Rosso = Deep Red (1975-2025)": ("Claudio Simonetti's Goblin", "Profondo Rosso"),
    "Mi-Sex | Computer Games (Piou Piou Piou)": ("Mi-Sex", "Computer Games"),
    "The Beatles | White Album": ("The Beatles", "The Beatles"),
    "Terence Trent D'Arby | Introducing the Hardline According to Terence Trent D'Arby": ("Terence Trent D'Arby", "Introducing the Hardline"),
    "Eurythmics | Sweet Dreams (Are Made of This)": ("Eurythmics", "Sweet Dreams (Are Made of This)"),
    "AC/DC | Dirty Deeds Done Dirt Cheap (edición australiana)": ("AC/DC", "Dirty Deeds Done Dirt Cheap"),
    "The Blackbyrds | City Life": ("The Blackbyrds", "City Life"),
    "David Byrne | Songs from The Catherine Wheel": ("David Byrne", "The Catherine Wheel"),
    "David Bowie | \"Héros\" / V-2 Schneider (simple francés)": ("David Bowie", "\"Heroes\""),
    "Count Basie | Basie at Birdland": ("Count Basie and His Orchestra", "Basie at Birdland"),
}

# Por defecto se busca el álbum (si no, MusicBrainz a veces devuelve el simple homónimo y la tapa
# sale mal). Acá van los que sí son simples/maxis o compilados.
TIPO = {
    "Lenny Kravitz | I Build This Garden for Us": 'single',
    "The Chemical Brothers | Galvanize (12\")": 'single',
    "Madonna | Music (single, no el álbum)": 'single',
    "Madonna | American Life (Missy Elliott American Dream Remixes)": 'single',
    "Divine | Love Reaction": 'single',
    "Mi-Sex | Computer Games (Piou Piou Piou)": 'single',
    "The Prodigy | Everybody in the Place": None,
    "Stevie Wonder | Original Musiquarium I": None,
    "Elvis Presley | The Sun Sessions": None,
    "Madonna | American Life [promo sin identificar: Love Profusion / Nobody Knows Me / Nothing Fails]": None,
    "David Bowie | \"Héros\" / V-2 Schneider (simple francés)": 'single',
    "Allan Holdsworth | Road Games": 'ep',
    "Banda Mel | Prefixo de Verão": None,
}


def search(qa, qd, tipo=None):
    lu = f'releasegroup:"{qd}" AND artist:"{qa}"' + (f' AND primarytype:{tipo}' if tipo else '')
    url = 'https://musicbrainz.org/ws/2/release-group/?' + urllib.parse.urlencode({'query': lu, 'fmt': 'json', 'limit': 3})
    for _ in range(3):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30)).get('release-groups', [])
        except Exception:
            time.sleep(3)
    return []


if __name__ == '__main__':
    out = json.load(open(OUT)) if os.path.exists(OUT) else {}
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    for r in disc_rows(conn):
        k = key(r)
        if k in out:
            continue
        q = Q.get(k, (r['artista'], r['titulo']))
        if q is None:
            out[k] = None
            continue
        rg = search(*q, tipo=TIPO.get(k, 'album'))
        rg = [x for x in rg if not set(x.get('secondary-types', [])) - {'Live', 'Soundtrack'}] or rg
        out[k] = rg[0]['id'] if rg else None
        print(k, '->', rg[0]['title'] if rg else None, flush=True)
        time.sleep(1.2)
    json.dump(out, open(OUT, 'w'), ensure_ascii=False, indent=0)

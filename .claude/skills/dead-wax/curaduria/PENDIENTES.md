# Curaduría en curso (sep 2026)

Estado al 27/09/2026, para retomar en una sesión nueva sin perder nada.
Leer esto antes de seguir con cualquier compra, carga a la base o la página de la feria.

## 1. Página de la feria (artifact)

- Link: https://claude.ai/artifact/DVryBYPAcqAX3scZDRqmu5 (privado; Ana lo comparte desde Share).
- Fuente: `feria-2026-09/feria-dead-wax.html` (republicar con la tool Artifact pasando ese `url`, para no crear otro link).
- Estilo: igual a anavare.la (repo `rawwwpower/anavare-la`): fondo `#1c1c1a`, Switzer + Geist Mono embebidas, grises zinc, minúsculas.
- Formato pedido por Ana: un renglón por disco, escaneable, con **toda** la info de la tabla (edición, estado disco/tapa, alertas, porqué completo, precio en pesos y USD a $1.600). No recortar datos.
- Debe ser **liviana** (poca señal): nada externo en runtime; tapas embebidas como JPEG 88×88 (~2-3 KB c/u).
- Datos: `feria-2026-09/full_data.js` (48 discos: 14 destacados, 28 también, 6 evitar). Lista original del proveedor: `lista-proveedor.txt` (561 ítems).

### Tapas: PENDIENTE

- `mbids.json`: release-group de MusicBrainz para 44 de 47 títulos (sin tapa: Milton *Paixão e Fé*, y los bootlegs de Talking Heads y Boston).
- `covers.py` baja `front-250` de Cover Art Archive, reduce a 88×88 y guarda `covers.json` (data URIs). Después, meter ese JSON en `const COVERS = {}` de la página (clave `"Artista | Título"`) y republicar.
- Contacto para el User-Agent de MusicBrainz: variable de entorno `MB_CONTACT` (pedírselo a Ana; nunca usar su email principal).
- Bloqueo: Cover Art Archive redirige a `dnXXXXXX.ca.archive.org` / `iaXXX.us.archive.org`. Ana agregó `*.ca.archive.org` y `*.us.archive.org` en Network access, pero en la sesión anterior el proxy seguía rechazándolos. Probar primero: `curl -sS -o /dev/null -w "%{http_code}" https://dn710703.ca.archive.org/`.

## 2. Javierfan (javierfandiscos.com.ar)

Elegidos por Ana. Dijo que "compró algunos" pero **no confirmó cuáles**: preguntar antes de cargarlos como `owned`.

| Disco | Edición | Precio web | Nota |
|---|---|---|---|
| AC/DC · Dirty Deeds Done Dirt Cheap | Europa 1979, Atlantic ATL 50 323 | $71.600 | impecable |
| Eurythmics · Sweet Dreams | UK 1983, RCA RCALP 6063 | $57.900 | tic en el 4º tema del lado A |
| Stevie Wonder · Original Musiquarium | UK 1982, Motown TMSP 6012, 2 LP | $86.350 | compilado, Precision Lacquer |
| David Bowie · Station to Station | UK 1976, RCA APL1-1327 | $86.400 | exc++ |
| Hawkwind · Hall of the Mountain Grill | UK 1974, UA UAG 29672 | $73.700 | con Lemmy; sticker arrancado |
| Bob Marley · Rastaman Vibration | UK 1976, Island ILPS 9383 | $92.700 | etiqueta = Discogs r844464 (Rondor Music); vendedor confirma STERLING en matrix → primera prensa |

- Catálogo completo de la web con stock y descripciones: `javierfan-2026-09/catalogo-web.json`. Lookups de Discogs: `discogs-lookup.json`.
- En MercadoLibre (JAVIERFAN1) los mismos discos salen ~8-12% más caros; comprar por la web.

## 3. Otros pendientes

- **Aerosmith · Rocks** (Japón, CBS/Sony 25AP 78, 1976, Discogs r1471651 o variante): falta precio y si tiene obi. Sin obi, razonable $35-55 mil.
- **AC/DC · Back in Black** (ya `owned`, id 21): confirmar cuál de las 8 variantes alemanas con foto de etiqueta y dead wax.
- **Walter Carlos · Electronic Bach** (ya `owned`, id 22): falta edición (país, sello, catálogo).
- **Elvis buscados**: *The Sun Sessions*, *From Elvis in Memphis*, *Elvis Presley* (1956). Los de Javier con stock no valían la pena.
- **Hawkwind buscado**: *Doremi Fasol Latido*, UK original United Artists (el favorito de Ana).

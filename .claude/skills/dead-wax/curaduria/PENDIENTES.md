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

### Tapas: HECHO (27/09, versión 5 del artifact)

- 43 de 47 títulos con tapa embebida (88×88 JPEG, ~120 KB en total; la página pesa ~173 KB). Revisadas a ojo con una hoja de contacto.
- Sin tapa (quedan con iniciales): Milton *Paixão e Fé* (no está en MusicBrainz), Schoener *Video Magic* (ningún release tiene arte en Cover Art Archive) y los bootlegs de Talking Heads y Boston.
- Corregidos en `mbids.json`: Queen I (apuntaba a un compilado de 1981) y Draw the Line (apuntaba al simple).
- Cómo baja `covers.py`: los nodos `dnXXXXXX.ca.archive.org` / `iaXXX.us.archive.org` **siguen bloqueados** por el proxy aunque estén en Network access. El script toma el identificador del item de la redirección de Cover Art Archive y baja `archive.org/services/img/<item>` (miniatura de ~180 px, servida directo por archive.org). Para reintentar algunos: `python3 covers.py "Artista | Título" ...` (los suma a `covers.json`).
- Para agregar tapas a discos nuevos: sumar el MBID a `mbids.json`, correr `covers.py` con esas claves y reemplazar el objeto `COVERS` de la página con el contenido de `covers.json`.

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

# Curaduría en curso

Estado al 04/10/2026, para retomar en una sesión nueva sin perder nada.
Leer esto antes de seguir con cualquier compra, carga a la base o la página de vinilos.

## Dónde vive cada cosa

- **Todo disco (tenido o querido) está en `data/coleccion.db`.** Colección = `status=owned`; wishlist =
  discos con `prioridad` (`iconico` / `top` / `interesante` / `evitar`), con `resumen`, `etiquetas` y `fuente`.
  Desde el 03/10/2026 ahí está también lo que antes vivía en tablas sueltas (la feria, los elegidos de
  Javierfan, los buscados), así que no hay que mantener listas aparte.
- **La página "vinilos"** (https://claude.ai/artifact/DVryBYPAcqAX3scZDRqmu5) se genera desde la base:
  ver `vinilos/README.md`. Formato pedido por Ana: un renglón por disco, escaneable, con toda la info
  (edición, estado disco/tapa, alertas, el porqué completo, precio en pesos y USD a $1.600), y liviana
  (nada externo; tapas embebidas).
- Fuentes crudas: `feria-2026-09/lista-proveedor.txt` (561 ítems de la feria) y
  `javierfan-2026-09/catalogo-web.json` (catálogo de la web con stock; en MercadoLibre, JAVIERFAN1,
  los mismos discos salen ~8-12% más caros: comprar por la web).

## Antes de cualquier recomendación

Leer en `SKILL.md` "No confiar: verificar", "un disco es un activo" y el **protocolo de identificación**
(niveles de confianza confirmada / probable / sin confirmar). Lo que dice la base es hipótesis hasta verificarlo.

## Abierto

- **Madonna · Music** (wishlist, #26): en Maniac hay dos reediciones (negra 2020, barcode 093624786511, y azul 2026,
  081227924034), con el mismo master: elegir por precio. La original 2000 hay que buscarla usada y confirmarla por dead wax.
- **Icónicos** (9, con ranking de versiones en la tabla `versiones`): Black Sabbath, AIC *Facelift* y *MTV Unplugged*,
  *Blood Sugar Sex Magik*, *Mezzanine* (año de la reedición de Maniac a confirmar: el barcode 602537540433 es de
  2013, 2017 o 2023), *Play*, *Sonic Temple*, *White Album* (la US SWBO-101 es "evitar") y *Dig Your Own Hole*.

- **AC/DC · Back in Black** (owned, id 41): confirmar cuál de las 8 variantes alemanas, con foto de
  etiqueta y dead wax.
- **Walter Carlos · Electronic Bach** (owned, id 51): falta la edición (país, sello, catálogo).
- **Aerosmith · Rocks** (wishlist): falta precio y si tiene obi.
- **London Records** (londonrecords.com.ar, 03/10): preguntar al vendedor el catálogo de Led Zeppelin IV
  (¿P-8166A?), qué es el T-Wave "color azul", qué edición es el Blood Sugar Sex Magik "limitado", si Hot
  Space trae obi, y fotos de etiqueta/matrix de los AC/DC australianos. Las fotos de la tienda
  (acdn-us.mitiendanube.com) están bloqueadas por el proxy del sandbox: hay que pedírselas a Ana.
- `coleccion.py list --incomplete` para la próxima ronda de repaso con Seba.
- **"Listado de Gaby"** (04/10): no está en el repo. Se asumió que es la lista de la feria (copias repetidas del
  mismo disco) y se respondió cuál copia conviene; si es otra lista, pedírsela a Ana.
- Feria, 14 hallazgos nuevos (ids 160-173): todos "sin confirmar" (solo datos de la lista). Preguntar el estado
  de King Crimson *Earthbound* (¿UK Island HELP 6?) y si Synergy *Cords* es el vinilo transparente.
- Tapas que faltan (quedan con iniciales): Milton *Paixão e Fé*, Schoener *Video Magic*, Favio
  *Nazareno Cruz y el Lobo*, *Orange Mécanique*, Lennon *Shaved Fish*, Divine, Jack de Mello,
  Mister Sam, Elvis *Elvis Presley*, White Album y los bootlegs. No están (o no bien) en MusicBrainz.

## Hecho

- 27/09: página de la feria con tapas embebidas.
- 03/10: compras en Javierfan cargadas (Dirty Deeds, Sweet Dreams, Musiquarium, maxi de Kravitz).
  Siguen en la wishlist Bowie *Station to Station*, Hawkwind *Hall of the Mountain Grill* y Marley
  *Rastaman Vibration*.
- 03/10: review de London Records: 9 pedidos por Ana + 15 hallazgos de la web, todo en la base (fuente "london records 2026-10").
- 03/10: la página pasa a ser "vinilos": colección + wishlist + buscador, generada desde la base.
- 03-04/10: icónicos como fichas con ranking de versiones (país, cómo suena, cómo reconocerla); wishlist primero,
  chips de sección/estilo, lupa; las red flags ya no se muestran.
- 04/10: error con *Music* (SKU = barcode compartido) → protocolo de identificación en SKILL.md y revisión de fichas.
- 04/10: segunda pasada a la lista de la feria (el PDF = `feria-2026-09/lista-proveedor.txt`): 14 hallazgos nuevos
  (jazz/fusión, funk, art pop, axé) + el bootleg de Gabriel como evitar; respuesta sobre las copias repetidas.

# Curaduría en curso

Estado al 07/10/2026, para retomar en una sesión nueva sin perder nada.
Leer esto antes de seguir con cualquier compra, carga a la base o la página de vinilos.

## Retomar acá (24 oct 2026, cierre): ronda de fotos para completar la colección de Ana y Seba

Ana manda fotos de etiqueta, tapa o dead wax y voy identificando y cargando cada disco. Lo mínimo que alcanza: la etiqueta
del lado A (catálogo, sello, "Made in"), o esos tres datos escritos; el dead wax solo para confirmar primeras prensas. Cada
foto se resuelve con ficha corta + dato curioso buscado, carga silenciosa en la base, `build.py` y republicar vinilos.
Si MusicBrainz no tiene la tapa, recorto la foto de Ana a 88 px y la meto en **`curaduria/vinilos/covers.json`** (así
quedaron 2001, los tres de Yupanqui y Ben E. King); al tocar **`mbids.json`** a mano, guardarlo con `indent=0`.
Nuevos (ids **201-214**): Seba: Rocks JP 25AP 78 primera prensa 1976, Almendra *En Obras / 1* ML-712, Yupanqui
(*Preguntitas sobre Dios* y *Campesino* Le Chant du Monde, *El payador perseguido* Odeon LDI-205 en dos copias, una sola
ficha), Charly *Cómo conseguir chicas* promo CBS 70.032 (título deducido por los temas, falta foto de tapa). Ana: 2001
MGM S1E-13 ST (falta etiqueta para el año), Ben E. King Vinyl Passion (lista negra, fue un regalo), Blondie *Eat to the
Beat* UK CDL 1225, Babasónicos *Jessico* y *Trance Zomba* (reediciones Sony), B-52's BSK 3355, Cobham *Spectrum* SD 7268
(de ahí sale el sample de Safe from Harm) y *Shabazz* licencia Music Hall. Confirmados con foto: **Vol. 4 (id 3) primera
prensa UK en los dos lados** (1Y//1 PORKY, 2Y//1 PECKO), Dirty Deeds (id 81, alemán WEA), Back in Black (id 41, alemán WEA
con SACEM), Toys in the Attic de Seba (id 57, RSD 2013 Nº 4303), Sabbath Bloody Sabbath (id 23), Debut de Seba (id 20).
Toxicity de Seba (id 17): barcode, reedición 2018. Decidido: el *Rocks* sale de la wishlist de Ana (Seba ya lo tiene,
id 133 queda como evaluado); nueva en wishlist **id 215, tapa gatefold 1ª tirada para el Vol. 4** (código "VO", sin
duraciones adentro, librito de 4 páginas pegado), prioridad interesante. Abierto (Ana/Seba, fotos): lado B del Rocks,
etiquetas de Yupanqui y del 2001, tapa del Charly, Master of Reality y Future Shock de Seba, Led Zeppelin II y Nena de
Ana, Electronic Bach. `coleccion.py list --incomplete` lista el resto.

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

- **AC/DC · Back in Black** (owned, id 41): etiqueta vista el 24/10/2026 (alemana WEA con recuadro SACEM). Para saber
  cuál de las 8 variantes alemanas es, falta el dead wax completo de los dos lados.
- **Walter Carlos · Electronic Bach** (owned, id 51): falta la edición (país, sello, catálogo).
- **London Records** (londonrecords.com.ar, 03/10): preguntar al vendedor el catálogo de Led Zeppelin IV
  (¿P-8166A?), qué es el T-Wave "color azul", qué edición es el Blood Sugar Sex Magik "limitado", si Hot
  Space trae obi, y fotos de etiqueta/matrix de los AC/DC australianos. Las fotos de la tienda
  (acdn-us.mitiendanube.com) están bloqueadas por el proxy del sandbox: hay que pedírselas a Ana.
- `coleccion.py list --incomplete` para la próxima ronda de repaso con Seba.
- **Fotos de etiqueta y dead wax** para pasar a "confirmada": Mr. Gone (Master Sound), Led Zeppelin II japonés
  (¿Nippon Grammophon 1969 o Warner-Pioneer?), Go-Go's Vacation (y qué dice el sello negro del obi), Nena
  (¿cuál de las dos copias de la lista?) y Jaco (MOV 2010 o represión posterior).
- **Penguin Cafe Orchestra**: la copia de la feria se vendió; buscar otra (japonesa 28MM 0065 o UK Editions EG 1981).
- **"Listado de Gaby"** (04/10): no está en el repo. Se asumió que es la lista de la feria (copias repetidas del
  mismo disco) y se respondió cuál copia conviene; si es otra lista, pedírsela a Ana.
- Feria, 14 hallazgos nuevos (ids 160-173): todos "sin confirmar" (solo datos de la lista). Preguntar el estado
  de King Crimson *Earthbound* (¿UK Island HELP 6?) y si Synergy *Cords* es el vinilo transparente.
- Tapas que faltan (quedan con iniciales): Milton *Paixão e Fé*, Schoener *Video Magic*, Favio
  *Nazareno Cruz y el Lobo*, *Orange Mécanique*, Lennon *Shaved Fish*, Divine, Jack de Mello,
  Mister Sam, Elvis *Elvis Presley*, White Album y los bootlegs. No están (o no bien) en MusicBrainz.

- **Goblin**: búsqueda continua de buenas prensas, sobre todo Cinevox italianas originales (la *Suspiria* MDF 33/108
  ya se evaluó y no se compró, id 13).
- **Fundas exteriores para gatefold**: polipropileno de 3 a 4 mil, 325 mm o más, en MercadoLibre. El anuncio tiene que
  decir "polipropileno" explícito (para evitar PVC). Referencias: MoFi, Sleeve City, Bags Unlimited (casi todo requiere
  importar).
- **Wishlist de escucha** (pila de Ale, 21/10, ids 194-198): elegir edición y catálogo de cada una cuando aparezcan.

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
- 04-07/10: compras de la feria a la colección (Mr. Gone, Led Zeppelin II, Go-Go's, Nena) y Jaco Pastorius (MOV).
  Gustos nuevos en SKILL.md (fusión oscura/electrónica, Future Shock, Björk Debut; no Pink Floyd).
  Wishlist de Seba (Steely Dan, YMO; la página marca "para seba"). nana sale de main: queda en `claude/nana-ipod`.

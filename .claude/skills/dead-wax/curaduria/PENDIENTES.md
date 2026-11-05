# Curaduría en curso

Estado al 07/10/2026, para retomar en una sesión nueva sin perder nada.
Leer esto antes de seguir con cualquier compra, carga a la base o la página de vinilos.

## Retomar acá (5 nov 2026): panorama de Spotify

Ana pasó el export de sus playlists de Spotify. Lo que quedó está en `references/panorama-spotify.md`, que es contexto
para recomendar y no una wishlist. Se cargaron: *Maggot Brain* (owned, edición sin identificar, id 300), y como `top`
*Cymande* (301), *Freedom Flight* (302) y los cuatro discos de estudio de Kyuss (303-306). Abierto: relevar la primera
edición de cada uno (`versiones`). Mezcla con BPM y tonalidad: por ahora no, solo si Ana lo pide.

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

## Para escuchar (Ana)

**Tags rápidos de Ana (02/11/2026)** al pasar un link: `+` = me gusta / lo conozco (wishlist, etiqueta *referencia de gusto*); `?` = guardar para escuchar (etiqueta `para escuchar`, pestaña de la página); `-` = no me gusta / descartar. Link sin tag: preguntar.

Discos que Ana dijo que va a escuchar. Cuando vuelva, preguntarle qué le parecieron, anotar su opinión en `review` y sacarlos de esta lista. Si algo no le gustó, preguntar si sale de la wishlist. **Regla (pedido de Ana, 02/11/2026):** cada vez que diga "después escucho" o deje algo para más tarde, cargarlo en la base con la etiqueta `para escuchar` (y el link de la tienda en `fuente`): aparece en la pestaña **para escuchar** de la página vinilos, con links a la tienda y a YouTube. Si no está para comprar, va con `status=descubrimiento`; al escucharlo, sacarle la etiqueta y decidir (wishlist o nada).

- **Desde el 02/11/2026, veta goth y post-punk, de Fear of Musik.** Orden sugerido:
  - [Sisters of Mercy, *The Reptile House E.P.*](https://fearofmusik.com.ar/rock/post-punk-goth/the-sisters-of-mercy-reptile-house-ep-vinilo-12-uk-1983-insert-goth): está en la wishlist; empezar por *Kiss the Carpet*.
  - [Bauhaus, *Kick in the Eye*](https://fearofmusik.com.ar/rock/post-punk-goth/bauhaus-kick-in-the-eye-satori-vinilo-12-uk-1981-goth)
  - [Killing Joke, *Requiem*](https://fearofmusik.com.ar/rock/post-punk-goth/killing-joke-requiem-vinilo-12-uk-1980-post-punk)
  - [The Mission, *God's Own Medicine*](https://fearofmusik.com.ar/rock/post-punk-goth/the-mission-uk-gods-own-medicine-vinilo-lp-promo-usa-1987-goth-rock)
  - [Alien Sex Fiend, *Ignore the Machine*](https://fearofmusik.com.ar/industrial-electro-ebm/alien-sex-fiend-ignore-the-machine-vinilo-12-uk-1984-industrial-goth): el más raro, dejarlo para el final.

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
- **Monkey Records** (monkey-records.com, 31/10/2026): todo nuevo, fuerte en metal, prog y grunge, algo de jazz. El stock
  completo con barcode sale de su API (`/wp-json/wc/store/v1/products?per_page=100&page=N`). Lo evaluado está en la base
  con `fuente` "Monkey Records 2026-10"; lo aprendido de sus ediciones, en `references/casos-especificos.md`.

## Antes de cualquier recomendación

Leer en `SKILL.md` "No confiar: verificar", "un disco es un activo" y el **protocolo de identificación**
(niveles de confianza confirmada / probable / sin confirmar). Lo que dice la base es hipótesis hasta verificarlo.

## Curaduría Muzik Saved My Life (05/11/2026, abierta: esperando qué le interesa a Ana)

Tienda de CABA (muziksavedmylife.com, WooCommerce: el catálogo entero sale de `/wp-json/wc/store/v1/products?per_page=100&page=N`, 2217 ítems, 2143 en stock; la descripción trae Sello/Catálogo/Formato/País/Año/Disco/Tapa, así que se puede filtrar por "Reissue"). Fuerte en 12" de synth-pop/house/Depeche/Madonna. Precios ARS al 05/11/2026.

Segunda pasada (la buena, después de la corrección de Ana):
- 💎 Cocteau Twins *Victorialand* Japón 1986 Virgin/4AD 25VB-1092, NM/NM, $328.821 (caro, sin referencia chequeada) · New Order *Thieves Like Us* 12" Japón 1984 Factory YW-7420-AX, NM/EX, $112.098.
- 👍 Cocteau Twins *Head Over Heels* Francia 1983 New Rose ROSE 25, NM/NM, $112.098 · Siouxsie *Candyman* 12" UK 1986 SHEX 10, NM/NM, $74.732 · Gang of Four *Solid Gold* USA 1981 BSK 3565, NM/EX, $84.403 · Dusty Springfield *Dusty in Memphis* USA 1969 SD 8214, NM/NM, $168.806 (original no audiófilo; la que mejor suena es Analogue Productions 45 rpm) · Nina Hagen Band *Unbehagen* 1979 CBS 84159, NM/NM, $42.202.
- Oportunidades baratas (maxis de época): Moskwa TV *Tekno Talk* 1985 $32.355 · White Door *Kings of the Orient* Clay 1982 $43.608 · Gary Clail/On-U *Escape* 1991 $44.312 · George Kranz *Trommeltanz* 1983 $46.334 · DAF *Voulez Vous Coucher Avec Moi* 1986 $55.390 · Art of Noise *Paranoimia* UK 1986 $59.786 · A Split-Second *Take This and Shove It* 1987 $97.222.
- Metal japonés de época: Ozzy *Bark at the Moon* 30AP 2731 $106.295 · Tygers of Pan Tang *The Cage* VIM-6285 $104.625.
- Tercera pasada (pedido de Ana: "busca con más intensidad", leídos los 1666 ítems sin Depeche/Erasure/Madonna):
  - Veta Future Shock/Technodelic: **Propaganda *Dr. Mabuse* 12" ZTT 1984 $35.168 (💎 barato)** · Patrick Cowley *Goin' Home / Tech-No-Logical World* 12" Alemania 1983 $68.226 · Debbie Harry *Rush Rush* 12" Japón 1984 (Moroder, *Scarface*) $67.259 · Off *Electrica Salsa* 12" 1986 (Sven Väth) $85.282 · The Assembly *Never Never* Mute 1983 $55.390 · Vicious Pink *Fetish* UK 1985 $93.811 · Two Sisters *B-Boys Beware* 1983 $78.460 · The System *You Are In My System* 1983 $110.867 · Hypnopedia 1989 $89.942 · THK *France* Warp 1992 $82.205.
  - Post-punk/indie: New Order *The Perfect Kiss* 12" Japón 1985 $98.470 y *Bizarre Love Triangle* Bélgica 1986 $112.538 · Psychedelic Furs *Heaven* 12" 1984 $65.412 · Simple Minds *The American* 12" UK 1981 $30.948 · Stan Ridgway *Camouflage* UK 1986 $30.948 · OST *Dogs in Space* USA 1986 (Iggy, Boys Next Door, Gang of Four, Eno) $84.403.
  - Rave/breakbeat/jungle: Bomb the Bass *Beat Dis* UK 1988 $62.142 · M|A|R|R|S $75.963 · 808 State *Lift* $62.142 · Higher Sense *Lock Up* Moving Shadow 1996 $34.289 · Swag *Dark Corners* Jus' Trax $87.041 · Floorplan M-Plant $58.361.
  - Dub: Gary Clail & On-U *Escape* / *Human Nature* ~$44k c/u · Peter Tosh & Mick Jagger 12" promo 1978 $67.048. Bandas sonoras: Queen *Flash Gordon* USA 1980 $39.564. Hip hop: Run-DMC *Here We Go* promo 1985 $134.518.
  - No hay: cumbia, jazz, hip hop 2000s, hardcore; Spice Girls solo reedición 2019.
- Primera pasada, vigente pero tibia para Ana: Quincy Jones *The Dude* USA 1981 SP-3721 $93.811 · Chas Jankel 12" Francia 1982 $102.339 · Grace Jones *Slave to the Rhythm* 12" USA 1985 $65.412 (Ana busca *Warm Leatherette*, id 31) · Horace Andy *Midnight Scorchers* · Rhythm & Sound *w/ The Artists* · *Virtual Dreams II* · *Congo Funk!* · Pastoral 1973.
- Descartados por Ana: *Rockit* (ya está *Future Shock* en casa), *Sonic Temple* Brasil (tiene la US de época, id 34 owned), *Álbum Blanco* argentino, Aquelarre.

## Abierto

- **Gusto de Ana, ronda Fear of Musik (02/11/2026):** Ana pasa discos que le llaman la atención o conoce, para que conozca su gusto. Se cargan en la wishlist como `interesante` con la etiqueta "referencia de gusto". Señal nueva: maxis de hip hop de los '90 y 2000 con historia de sampleo (Coolio *Gangsta's Paradise*, Eminem *Lose Yourself*, Crazy Town *Butterfly*) , el rap rock con samples de rock (Beastie Boys *Licensed to Ill*), big beat y rave con samples (Rockafeller Skank, Prodigy *Out of Space*), Primus ("me gusta mucho"), los Doors ("me gustan") y pop mainstream en maxis de remixes (Britney *Oops!*). Tenerlo en cuenta en las búsquedas, junto con los maxis largos para mezclar. **Ana avisó que su gusto es mucho más amplio y curioso que lo que muestra la colección:** no recomendar solo por artistas o géneros que ya tiene; buscar por conexiones (samples, productores, historias, cruces de género) y animarse a sugerir cosas fuera de lo esperable. Al recomendar discos de una tienda, **poner el link a cada uno** (pedido de Ana, 02/11) para que los vea rápido.
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
  Wishlist de Seba (Steely Dan, YMO; la página marca "para seba"). nana se mudó al repo `musica` (05/11).

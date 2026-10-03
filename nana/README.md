# nana

Una webapp liviana con forma de iPod nano (4ª generación, verde, 2005) que
lleva adentro la colección de Dead Wax. Publicada como artifact en
https://claude.ai/artifact/FgBLCH8DMS3cbLAYpHn45d (privado; Ana la comparte desde Share).

**Se genera desde `data/coleccion.db`. No editar `nana.html` a mano.**

| Archivo | Qué es |
|---|---|
| `template.html` | El aparato: carcasa, click wheel, menús, reproductor, fotos, búsqueda. Sin datos. |
| `build.py` | Arma `nana.html` con la base (reusa las reglas y las tapas de `curaduria/vinilos/`), más los samples de `media/`. |
| `media/sintetizar.py` | Sintetiza el sample de audio (un loop original, sin derechos de nadie). |
| `media/hacer-media.sh` | De ese audio saca `dead-wax-2005.mp3` y el video de muestra `dead-wax-2005.mp4` (disco girando, 320×240). |
| `nana.html` | El resultado, lo que se publica. Un solo archivo (~1,1 MB), sin backend. |

```
python3 nana/build.py      # después de cada cambio en coleccion.db
```

Después, republicar `nana.html` con la tool Artifact (mismo archivo en la misma sesión, o pasando el `url` de arriba).

## Qué hace hoy (v0.1)

- **Música**: colección de Ana y de Seba, wishlist (icónicos / top / interesantes),
  descubrimientos, artistas, estilos, canciones y buscar (con la tira de letras del iPod
  o tipeando). Cada disco abre su ficha: tapa, sello, catálogo, grading, resumen, reseña,
  prensado, notas y el ranking de ediciones de los icónicos.
- **Reproducir**: el sample "Dead Wax 2005" y lo que se cargue desde *Extras → Cargar
  música y videos* (lee los tags ID3 y la tapa con jsmediatags). Lo cargado queda en
  IndexedDB de ese navegador. Si un tema es de un artista de la colección, la ficha del
  disco lo ofrece con ⏯.
- **Videos**: el sample de video; al abrir uno el nano se acuesta y la pantalla queda
  apaisada, como el 4G con el acelerómetro.
- **Fotos**: todas las tapas en grilla.
- **Ajustes**: los nueve colores del nano 4G (cada uno con su fondo de aviso de siluetas) y el clicker.
- Click wheel: arrastrar en círculo para moverse, tocar MENU / ⏮ / ⏭ / ⏯, botón del centro para elegir.
  Teclado: ↑↓, Enter, Esc, espacio, `,` `.`. En *Reproduciendo*, la rueda es volumen; con el
  centro pasa a adelantar/atrasar (el rombito).

## Lo que viene (ver ROADMAP.md, Fase nana)

Reconocer lo que suena (tipo Shazam: el menú *Extras → Reconocer canción* ya está, todavía sin
función), audio y videos atados a cada disco, y escuchar desde la ficha.

# deadwax

App simple para llevar tu colección de discos, tu wantlist, y fusionarla con
la de Seba cuando escuchan música juntos.

## Uso

Abrí `index.html` en el navegador (o serví la carpeta con cualquier servidor
estático). Todo se guarda en el navegador (`localStorage`), no requiere
backend ni conexión.

- **Colección**: los discos que ya tenés, con un filtro **Yo / Seba /
  Fusión**. Fusión combina ambas colecciones (cada disco muestra de quién
  es) para armar la sesión de escucha juntos.
- **Wantlist**: los que buscás. Botón "Comprado" los pasa directo a tu
  colección.
- **Exportar/Importar**: backup en JSON, abajo de todo. Podés pedirle a
  Seba que exporte su colección y la importás para tenerla en Fusión.

## Escalar a futuro

La lógica de guardado vive toda en el objeto `Store` de `js/app.js`
(`getAll`, `saveAll`, `upsert`, `remove`). Para pasar a un backend real
(sync entre dispositivos, compartir colección, etc.) alcanza con reemplazar
esos métodos por llamadas a una API, sin tocar el resto de la UI.

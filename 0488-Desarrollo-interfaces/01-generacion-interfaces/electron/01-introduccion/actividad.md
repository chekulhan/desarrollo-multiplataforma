# Electron usando HTML

**Borrar lo que ya tenemos y empezar de nuevo, instalando electron, etc...!**

# Ejercicio: “Menú de cafetería con navegación básica”
## 🎯 Objetivo

Aprender a usar etiquetas `<a>` para navegar entre páginas locales en una aplicación Electron, simulando un pequeño menú digital de una cafetería.

## Descripción

Vas a crear una aplicación sencilla de escritorio para una cafetería.

- Inicio (index.html) — muestra el nombre de la cafetería y un enlace al menú.

- Menú (menu.html) — muestra algunos productos y un enlace para volver a inicio.

- Pedidos (pedidos.html) - un formulario GET para captar el pedido del cliente

- Resultado del pedido (confirm.html) - una página para mostrar el resultado del pedido.

Al hacer clic en los enlaces, la aplicación deberá cambiar de página dentro de la misma ventana de Electron.

![Electron con HTML](../../../../x-assets/0488/electron-act1.1.png)
![Electron con HTML](../../../../x-assets/0488/electron-act1.2.png)
![Electron con HTML](../../../../x-assets/0488/electron-act1.3.png)
![Electron con HTML](../../../../x-assets/0488/electron-act1.4.png)

## Ayuda

En la última página, tendremos que captar los datos que pasamos a través del querystring GET, para posteriormente mostrarles en la página. Usar Javascript y la clase URLSearchParams para colocar los valores en su ubicación de la página:

![Window Location](../../../../x-assets/0488/electron-act1.5.png)

Usando Chrome Dev Tools, echar un vistazo a:
```javascipt
const x = new URLSearchParams(window.location.search);
```

Por ejemplo:

```javascript
<script>
    window.onload = () => {
      const params = new URLSearchParams(window.location.search);
      

      document.getE....textContent = ;
    };
  </script>
```
---

## Cuando hayas terminado
### 1 
¿Qué ocurre si cambias win.loadFile('index.html'); por:

```javascript
win.loadURL('https://www.cebanc.com/');
```

### 2
El proceso principal (main process) es un event listener y puede reaccion ante eventos emitidos en el window, por ejemplo, resize(), minimize(), close():

```javascript
 // Listen to resize events
  win.on('resize', () => {
    const [width, height] = win.getSize();
    console.log(`Window resized to ${width}x${height}`);

    // Send resize info to renderer
    //win.webContents.send('window-resized', { width, height });
  });

  win.on('focus', () => console.log('Window focused'));
  win.on('blur', () => console.log('Window lost focus'));
  win.on('minimize', () => console.log('Window minimized'));
  win.on('maximize', () => console.log('Window maximized'));
  win.on('close', (e) => {
    console.log('Window is closing');
    // e.preventDefault(); // optional: stop closing
  });
  win.on('closed', () => console.log('Window closed'));
```

!Probarlo!

### 3

¿Podrias mandar un mensaje para mostrar que plataforma se esta usando? Por ejemplo, si es Mac, mostrar 'estas en un Mac'.

```javascript
app.whenReady().then(() => {
  console.log(process.platform);

```
En Mac, el resultado es 'darwin'.


### 4

```javascript

import { app, BrowserWindow } from 'electron';

let win1;
let win2;

function createWindows() {
  // First window
  win1 = new BrowserWindow({
    width: 600,
    height: 400,
  });
  win1.loadFile('index.html');

  // Second window
  win2 = new BrowserWindow({
    width: 500,
    height: 300,
  });
  win2.loadFile('second.html');
}

app.whenReady().then(createWindows);


```
---

## Respuesta
```javascript
<script>
    window.onload = () => {
      const params = new URLSearchParams(window.location.search);
      const nombre = params.get('nombre') || '(no ingresado)';
      const cafe = params.get('cafe') || '(no seleccionado)';

      
      document.getElementById('nombre').textContent = nombre;
      document.getElementById('cafe').textContent = cafe;
    };
  </script>
```

# Cuando hayas terminado
## 1 
¿Qué ocurre si cambias win.loadFile('index.html'); por:

```javascript
win.loadURL('https://www.cebanc.com/');
```

## 2
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

## 3

¿Podrias mandar un mensaje para mostrar que plataforma se esta usando? Por ejemplo, si es Mac, mostrar 'estas en un Mac'.

```javascript
app.whenReady().then(() => {
  console.log(process.platform);

```
En Mac, el resultado es 'darwin'.


## 4
¿Qué te cuenta este ejemplo sobre los procesos? ¿Puedes ver el process Main y los procesos Render en el Task Manager?


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
# Desktop multiplataforma

[Electron](https://www.electronjs.org/)

```bash
npm init -y
npm install electron
npm install --save-dev electronmon
```

Fijaos en type:module, main:main.js y los comandos de dev y start:

```json
{
  "name": "electron",
  "version": "1.0.0",
  "description": "",
  "main": "main.js",
  "type": "module",
  "scripts": {
    "dev": "electronmon .",
    "start": "electron .",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "electron": "^38.0.0"
  },
  "devDependencies": {
    "electron-reload": "^2.0.0-alpha.1"
  }
}

```


```bash
npm run dev
```


En las primeras actividades (01-introduccion), vamos a integrar HTML directamente en una aplicación de Electron.


## Tips para desarrollar

### Open DevTools in Electron


When the Electron window opens, press:

- Windows/Linux: Ctrl + Shift + I

- Mac: Cmd + Option + I

Or in the main createWindow() process:

```javascript

  win.loadFile('index.html');

  // Open DevTools automatically
  win.webContents.openDevTools();
```

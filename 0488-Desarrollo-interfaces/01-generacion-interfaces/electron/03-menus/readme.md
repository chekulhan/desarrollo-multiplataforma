# Procesos en Electron

Electron tiene dos procesos principales:

1. Main process (proceso principal)

- Es el “cerebro” de tu aplicación.

- Controla ventanas, menús, archivos, diálogos nativos, y todo lo que interactúa con el sistema operativo.

- Es donde escribes main.js.

2. Renderer process (proceso de renderizado)

- Es donde corre tu interfaz de usuario (React, HTML, CSS).

- Cada ventana de Electron tiene su propio renderer.

- Aquí es donde tu usuario ve la app y hace clic en botones, rellena formularios, etc.

## Comunicación entre procesos (IPC)

Como el main y el renderer son procesos separados, necesitan una forma de hablar entre ellos:

- IPC = Inter-Process Communication
(Comunicación entre procesos)

- En Electron se hace con:

    - ipcMain → para escuchar y enviar desde el proceso principal

    - ipcRenderer → para escuchar y enviar desde el proceso de UI (React)

## Ejemplo práctico en tu app

Usuario hace clic en un menú de Electron → esto ocurre en el main process:
```js
win.webContents.send('open-form'); // mensaje al renderer
```

React (renderer) escucha el mensaje:
```js
ipcRenderer.on('open-form', () => {
  setShowForm(true); // muestra el formulario
});
```

React actualiza el estado y el modal del formulario aparece en pantalla.
import { app, BrowserWindow } from 'electron';
import path from 'path';
import isDev from 'electron-is-dev'; // optional, to distinguish dev vs build

const createWindow = () => {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    }
  });

  const startURL = isDev
    ? 'http://localhost:5173' // Vite dev server
    : `file://${path.join(__dirname, 'react-app/dist/index.html')}`;

  win.loadURL(startURL);
}

app.whenReady().then(createWindow);

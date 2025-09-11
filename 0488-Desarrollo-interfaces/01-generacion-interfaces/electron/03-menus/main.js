import { app, BrowserWindow, Menu, dialog } from 'electron';
import path from 'path';
import isDev from 'electron-is-dev';

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
    ? 'http://localhost:5173'
    : `file://${path.join(__dirname, 'react-app/dist/index.html')}`;

  win.loadURL(startURL);

  const menuTemplate = [
    {
      label: 'File',
      submenu: [
        { label: 'New', click: () => console.log('New clicked') },
        { label: 'Open', click: () => console.log('Open clicked') },
        { label: 'Open Form', click: () => win.webContents.send('open-form') }, // Open form directly here
        { type: 'separator' },
        { role: 'quit' }
      ]
    },
    {
      label: 'Edit',
      submenu: [
        { role: 'undo' },
        { role: 'redo' },
        { type: 'separator' },
        { role: 'cut' },
        { role: 'copy' },
        { role: 'paste' }
      ]
    },
    {
      label: 'Help',
      submenu: [
        { label: 'About', click: () => console.log('About clicked') },
        { 
          label: 'About Me',
          click: () => {
            dialog.showMessageBox(win, {
              type: 'info',
              title: 'About Me',
              message: 'My Electron + React App\nVersion 1.0.0',
              buttons: ['OK']
            });
          }
        }
      ]
    }
  ];

  const menu = Menu.buildFromTemplate(menuTemplate);
  Menu.setApplicationMenu(menu);
}

app.whenReady().then(createWindow);

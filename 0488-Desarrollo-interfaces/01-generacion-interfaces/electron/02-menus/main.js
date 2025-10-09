import { app, BrowserWindow, Menu } from 'electron';

const createWindow = () => {
  const win = new BrowserWindow({
    width: 800,
    height: 600
  })

  win.loadFile('index.html');

  // --- Build menu ---
  const template = [
    {
      label: 'File',
      submenu: [
        {
          label: 'Start',
          click: () => {
            win.loadFile('start.html');
          },
        },
        {
          label: 'End',
          click: () => {
            win.loadFile('end.html');
          },
        },
        { type: 'separator' },
        { role: 'quit', label: 'Salir' },
      ],
    },
    {
      label: 'About Us',
      submenu: [
        { label: 'About Us', click: () => console.log('About Us clicked') },
      ],
    },
  ];


  const menu = Menu.buildFromTemplate(template);
  Menu.setApplicationMenu(menu);

}

app.whenReady().then(() => {
  createWindow()
})




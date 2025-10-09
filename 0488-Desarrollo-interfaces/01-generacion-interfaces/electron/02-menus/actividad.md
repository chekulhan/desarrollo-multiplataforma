# 5 Conceptos importantes sobre los menús

## 1. Los menús pertenecen al proceso principal
Los menús se definen en el **proceso principal (main process)**, no en las páginas HTML.  

Las páginas web (renderer) **no pueden crear menús nativos directamente**.

---

## 2. Plantillas de menú (menu templates)
Los menús se construyen a partir de **arrays de objetos**, llamados plantillas.  

Cada objeto puede tener:  
- `label` → lo que ve el usuario  
- `submenu` → elementos anidados  
- `role` → comportamiento predefinido  
- `click` → función personalizada que se ejecuta al hacer clic  

---

## 3. Roles como atajos
Los elementos con `role` (como `quit`, `copy`, `undo`) **manejan automáticamente el comportamiento específico de cada plataforma**.  

Esto te evita escribir funciones `click` repetitivas.

![Electron menu roles](../../../../../x-assets/0488/electron-menu-1.png)

---

## 4. Menú puede ser global o contextual
- **Menú de aplicación** → aparece en la parte superior de la ventana (`Menu.setApplicationMenu(menu)`).  
- **Menú contextual** → aparece al hacer clic derecho (usando `popup()` desde el renderer).  

Los menús pueden ser **dinámicos**, cambiando según el estado de la app.

---

## 5. Separadores y organización
Se usa `{ type: 'separator' }` para **agrupar visualmente los elementos**.  

Hace que los menús sean más claros y fáciles de usar.



# Actividades
## 1
Extender la aplicacion de pedidos de Café para incluir un menu de Electron

## 2
Recordar que tenemos el process, que es un objeto global de Node. Podrias usarlo para definir un menu específo para Windows y otro para Linux o Mac?
# 📖 Historia de React / ReactJS
## 🌱 Orígenes

2011 – Facebook tenía problemas de rendimiento en su aplicación web.

## 🚀 Lanzamiento público

Mayo de 2013 – Facebook libera React como open source en la conferencia JSConf US.

- Fue polémico porque introducía JSX, que mezclaba HTML con JavaScript (algo muy criticado en ese momento).
- Sin embargo, JSX y el concepto de Virtual DOM hicieron que React destacara en rendimiento y simplicidad.

## 🌍 Adopción y ecosistema

2014 – Empresas como Instagram empiezan a usar React.

2015 – Aparece React Native, para crear apps móviles con React.

2016 – Facebook lanza create-react-app (CRA), una herramienta para crear proyectos fácilmente.

2017–2018 – La comunidad crece enormemente. Frameworks como Next.js (2016) se vuelven populares para apps completas con React.

# Implementación
## CRA v Vite

CRA se volvió pesado, lento y difícil de personalizar.


 | Acción                         | Con **Create React App** (CRA) 🧓 | Con **Vite** (Recomendado) ⚡              |
| ------------------------------ | --------------------------------- | ----------------------------------------- |
| **Crear el proyecto**          | `npx create-react-app mi-app`     | `npm create vite@latest mi-app`           |
| **Elegir plantilla**           | No (solo React por defecto)       | Sí (React, React + TS, Vue, Svelte, etc.) |
| **Entrar al proyecto**         | `cd mi-app`                       | `cd mi-app`                               |
| **Instalar dependencias**      | (automático)                      | `npm install`                             |
| **Arrancar el servidor local** | `npm start`                       | `npm run dev`                             |
| **Build para producción**      | `npm run build`                   | `npm run build`                           |
| **Abrir preview de build**     | No directo (necesita `serve`)     | `npm run preview`                         |

*Create React App queda obsoleto (anunciado oficialmente en febrero 2025).*

La comunidad adopta Vite, Next.js, Remix y otros frameworks modernos.

React sigue siendo la librería de UI más popular del mundo.

## Vite
⚡ Ahora (Vite)

Crear proyecto
```bash
npm create vite@latest mi-app
```

👉 Te pregunta: ¿Qué framework quieres?
Eliges React (o React + TypeScript).

Instalar dependencias
```bash
cd mi-app
npm install
```

Arrancar servidor
```bash
npm run dev
```

👉 Super rápido, con hot reload inmediato.

Build y preview
```bash
npm run build
npm run preview
```

💡 En resumen:

CRA = fácil, pero viejo y lento.
Vite = moderno, flexible, rápido.


# Mi primer componente
Vamos a crear un componente y incluirlo en App.jsx

```jsx
const Greeting = () => {

    return (
        <>
            <h1>Hello from my component</h1>
        </>
    )
}

export default Greeting;
```

y lo incluimos en App.jsx:

```jsx
import Greeting from './components/Greeting.jsx'


<Greeting />

```

## Actividades

### Mi componente de presentación
🎯 Objetivo

Crear un componente React que muestre una tarjeta de presentación personal con:

- Un nombre
- Una imagen de perfil (puede ser un link de internet)
- Una breve descripción
- Un correo electrónico o dato de contacto

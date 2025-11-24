# Docker configuración

## Construir la imagen de Docker:
```bash
docker build -t unity-dev .
```
Construye una imagen de Docker usando el Dockerfile del directorio actual y le asigna el nombre/tag unity-dev. Esto prepara el entorno de desarrollo que usarás más adelante.


## Primera ejecución del contenedor (PowerShell)
```bash
docker run -it -v ${PWD}:/app --name unity unity-dev
```
Crea y ejecuta por primera vez un contenedor basado en la imagen unity-dev.

-it permite usar el contenedor de forma interactiva (consola).
-v ${PWD}:/app monta el directorio actual de tu máquina dentro del contenedor en /app, para compartir archivos.
--name unity asigna el nombre unity al contenedor para poder reutilizarlo después.

## Crear un proyecto dentro de /programs
```bash
dotnet new console
```
Crea una nueva plantilla de aplicación de consola usando .NET dentro del directorio /programs del contenedor. Esto genera un proyecto básico listo para compilar y ejecuta

## Compilar y ejecutar el proyecto
```bash
cd programs
dotnet run -c Release
```
Accede al directorio del proyecto y lo ejecuta en modo Release, lo cual compila la aplicación optimizada y la ejecuta.


## Volver a abrir el contenedor para seguir trabajando

Para ejecutar de nuevo:

```bash
docker ps -l
docker start -ai unity
```
# Demostración de clase

```python
with open("archivo.txt", "r") as f:
  s = f.read()

s = s.upper() # cambiar s a upper

with open("archivo.txt", "w") as f:
  f.write(s)
```


---


```python

# Leer linea por linea 

with open("archivo.txt", "r") as f:
    for line in f:
        print("LINE:", line.strip())

# Leer todos las lineas a una lista - comprobar el tipo de dato lines (type(lines)) 
with open("data.txt", "r") as f:
    lines = f.readlines()

print(lines)

# Leer los primeros 20 cáracteres
with open("data.txt", "r") as f:
    chunk = f.read(20)   # 20 chars

print(chunk)

# Leer una linea
with open("data.txt", "r") as f:
    line = f.readline()

print(line)

# Leer una imagen (binario) 'b'
with open("photo.jpg", "rb") as f:
    data = f.read()

print(len(data), "bytes read")
```


# ACTIVIDADES
**Tarea 1:**
Dado un archivo server.log, extraer solo las líneas que contengan "ERROR" (sin importar mayúsculas o minúsculas) 
y guardarlas en un archivo errors.txt.

server.log:
```
[2025-11-24 09:00:01] INFO: Servidor iniciado
[2025-11-24 09:01:05] INFO: Conexión establecida con el cliente 192.168.1.10
[2025-11-24 09:12:01] ERROR: No se pudo conectar a la base de datos
[2025-11-24 09:15:45] WARNING: Memoria disponible baja
[2025-11-24 10:05:22] ERROR: Usuario no autorizado
[2025-11-24 10:10:00] INFO: Proceso completado
```

Resultado final en errors.txt:
```
[2025-11-24 09:12:01] ERROR: No se pudo conectar a la base de datos
[2025-11-24 10:05:22] ERROR: Usuario no autorizado
```


**Tarea 2:**
Leer notas.txt:

```
Juan ha aprobado la materia de matemáticas.
Ana necesita mejorar en ciencias.
Pedro ha aprobado con excelente calificación.
Luisa no aprobó el examen de historia.
```
y mostrar el resultado en results.txt:

```
Número de líneas con la palabra 'aprobado': 2
```

**Tarea 3:**

En un archivo de 'clientes_local.txt', queremos aplicar un proceso de seguridad para quitar datos 
privados, antes de mandarselo por correo electrónico. 

```
Juan Pérez, juan@gmail.com, 453
Alicia López, alicia@yahoo.com, 143
```
Queremos conseguir el siguiente output en 'clients_global.txt':

```
Juan Pérez, <oculto>, 453
Alicia López, <oculto>, 143
```

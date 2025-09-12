# Actividades de funciones

## Actividad 1 - Odd and Even
Este código compara si un numero es par o impar, usando el comando mod %. Convertirlo en una funcion reutilizable:

```python
x = 11

print(x%2) # mod
```

## Actividad 2 - Count letters

Crear la funcion count_letters() para mostrar el número de letras que hay en un string. Por ejemplo "Maria" es 5.

```python
user_name = input("Enter your name: ")
num_letters = count_letters(user_name)

print(f"Your name has {num_letters} letters.")
```

## Actividad 3 - Count letters

The syntax variable x[start:stop:step] in Python slices a string (or list, tuple, etc.):

start → index to start from (inclusive)

stop → index to stop at (exclusive)

step → how much to move forward each time (can be negative!)

Here, start and stop are omitted → the whole string is used.
```python
x[::1]
```

Ignorando espacios, "la ruta natural" es un "palíndromo" => larutanatural. Crear una funcion para comprobar que es un palíndromo.





## Respuestas


x = "civic"

a = x[::-1]
b = x[::1]
if a == b: print("Paldíndromo")

frutas = ["MANZANA", "pera", "NARANJA", "uva", "MELON"]

new_frutas = []
for fruta in frutas:
    if fruta.upper() == fruta:
      new_frutas.append(fruta)

print(new_frutas)

x = [fruta for fruta in frutas if fruta.upper() == fruta]
print(x)

# Actividades
# 1. Multiplicar los numeros por 10:
nums = [1, 2, 3]
# La respuesta deberia ser [10, 20, 30]


# 2. Remplezar los valores negativos por 0, y mostrar los positivos tal como estan.
nums = [1, -5, -7, 3, 6]
# La respuesta deberia ser: [1, 0, 0, 3, 6]

# 3. Mostrar las palabras con una longitud mayor a 3 (filtro). Mostrarles en mayúsculas (presentacion)
palabras = ["hi", "hello", "hola", "python"]

# La respuesta deberia ser: ["HELLO", "HOLA", "PYTHON"]

# 4. Mostrar el texto "Par" si un numero es par y mostrar el texto "Impar" si no lo es
numbers = [2, 6, 7, 3, 4, 8]


# Actividades avanzadas
# Convertir este programa en un list comprehension
squares = []
for x in range(1, 10):
    squares.append(x**2)

print(squares)


# list comprehension con dicionarios
grades = {'Alice': 85, 'Bob': 70, 'Charlie': 95, 'Diana': 60}

# Generar un diccionario de personas y sus notas, solo si la nota es > 70




# Respuestas
x = [i**2 for i in range(11)]
print({name:grade for name,grade in grades.items() if grade>70})
result = [n*10 for n in nums]
x = [n if n> 0 else 0 for n in nums]
print([p.upper() for p in palabras if len(p)>3])
new_numbers = ["Par" if i % 2 == 0 else "Impar" for i in numbers]
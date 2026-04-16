# Las funciones Lambda son funciones anónimas (sin nombre) que solo pueden contener una expresión.
# Una función lambda se usa cuando necesitas una función sencilla y de rápido acceso

def multiplicado_por5(c):
  return c*5
   
print(multiplicado_por5(5))

c = lambda y : y*5 # se lee asi - una funcion que acepta "y" y devuelve y*5  
 
print(c(5))

def sumar(a, b):
  return a + b
   
print(sumar(5,6))

# se lee asi - una funcion que acepta a y b y devuelve a +b
x = lambda a, b: a+b
print(x(5,6))
print((lambda a, b: a+b) (2, 3))

# ACTIVIDAD ES
# Crear unas funciones lambda para hacer matemáticas. Por ejemplo, restar y dividir
# Imprimir True si el valor  es positivo y False si no lo es. Por ejemplo, x = 10 produce True
# Mostrar 'Par si x is un par y 'Impar' si no lo es
# Con una lista de palabras words = ["cat", "house", "tree", "elephant", "sun"], sacar True si la palabra es large (longitud > 4)
# En lugar de mostrar 1 o 0 para la asistencia de alumnos = [1, 0, 1, 1, 0, 0, 1], queremos mostrar 'Presente' o 'Ausente'
# Con 

foods = [("apple", 95), ("burger", 550), ("salad", 150), ("pizza", 300)]

# Respuestas -------------------
is_even = lambda x: x % 2 == 0

mi_lista = [1, 2, 3, 4, 5, 6]

resultado = [is_even(num) for num in mi_lista]
print(resultado)


long_word = lambda w: len(w) > 4

words = ["cat", "house", "tree", "elephant", "sun"]

result = [long_word(w) for w in words]
print(result)



check_result = lambda x: "Pass" if x >= 70 else "Fail"

scores = [85, 60, 73, 40, 90]

result = [check_result(score) for score in scores]
print(result)




attendance = [1, 0, 1, 1, 0, 0, 1]

status = lambda x: "Present" if x == 1 else "Absent"

attendance = [1, 0, 1, 1, 0, 0, 1]

result = [status(a) for a in attendance]
print(result)



foods = [("apple", 95), ("burger", 550), ("salad", 150), ("pizza", 300)]

check_food = lambda item: (item[0], "Healthy" if item[1] <= 200 else "Unhealthy")

foods = [("apple", 95), ("burger", 550), ("salad", 150), ("pizza", 300)]

result = [check_food(f) for f in foods]
print(result)


foods = [("apple", 95), ("burger", 550), ("salad", 150), ("pizza", 300)]

check_calorias = lambda x: x > 100
print([check_calorias(f[1]) for f in foods])


# -----

z = lambda x: x>0

mi_lista= [5,6,-3,7,-1]
positivos = [z(num) for num in mi_lista]
print(positivos)

for num in mi_lista:
  print(z(num))

resultado = [(lambda x:x>0)(i) for i in mi_lista]
print(resultado)

number = -10
(lambda x: "Positive" if x>0 else "Negative")(number)

"""
Los decoradores en Python son funciones que envuelven otra función para añadirle comportamiento sin modificar su código original. Permiten ejecutar código antes y/o después de la función que decoran, o modificar su resultado.

Se usan para reutilizar lógica común como logging, control de acceso, medición de tiempo o validaciones, evitando repetir código en múltiples funciones.

"""
# DEMO

def decorator_antes_despues(func):  # 1. Pasar func como si fuera say_hello()

    def wrapper(): # 2. definimos un wrapper - aqui se pasan los parámetros
        print("Antes")
        result = func() # 3. llamar la funcion say_hello()
        print(result)
        print("Despues")
        return result
    
    return wrapper # 4. devolver el wrapper

@decorator_antes_despues # 5. Aplicar el decorador
def say_hello():
    return "Hello!"


result = say_hello()

"""
Para pasar parámetros, usar:
def wrapper(*args, **kwargs):
    return func(*args, **kwargs)
"""

# Actividad 1
# Crear un decorator para que cuando un usuario ejecuta la funcion delete_account, se imprime un mensaje para auditar (borrando cliente 4)
# OJO: Habrá que pasar un parámetro id a la funcion wrapper

def delete_account(id):
    print(f"deleting account {id}")

delete_account(4)

# Actividad 2
# Quermos aplicar un decorador para validar el nombre, antes de registrar un usuario
# Crear el decorador @validar_usuario para ejecutar la funcion registrar_usuario solo si hay un nombre de usuario. 
# Si no, mostrar un mensaje de error

registrar_usuario("Jon", 12)
registrar_usuario("", 9)
registrar_usuario("Maria", 20)

# --------


import time
from functools import wraps

def log_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Starting '{func.__name__}' at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")
        
        result = func(*args, **kwargs)  # Execute the decorated function
        
        end_time = time.time()
        print(f"Finished '{func.__name__}' at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        
        return result
    
    return wrapper

# Example of usage
@log_time
def my_function():
    time.sleep(2)  # Simulating a task that takes 2 seconds
    print("Function is running!")

my_function()


# Respuestas ---------
# Actividad 1
def log_wrapper(func):

    def wrapper(*args):
        print(f"User is deleting {args}")
        func(*args)

    return wrapper

@log_wrapper
def delete_account(id):
    print(f"deleting account {id}")

delete_account(4)




# --
# Actividad 2
def validar_usuario(func):
    def wrapper(*args, **kwargs):

        print(*args)
        if len(args[0]) > 0:
            return func(*args, **kwargs)
        else:
            print(f"Error con user {args}")
    return wrapper

@validar_usuario
def registrar_usuario(nombre, edad):
    print(f"Usuario {nombre} registrado con edad {edad}")


registrar_usuario("Jon", 12)
registrar_usuario("", 9)
registrar_usuario("Maria", 20)
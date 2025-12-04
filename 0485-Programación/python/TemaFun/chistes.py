import random

# Definimos cada chiste como función
def chiste1():
    print("¿Por qué la escoba está feliz? ¡Porque ba-rriendo!")

def chiste2():
    print("¿Cuál es el colmo de un electricista? ¡No tener corriente en casa!")


# Lista de funciones
chistes = [chiste1, chiste2]

# Elegir un chiste al azar
chiste = random.choice(chistes)

chiste()

# Actividad: Añadir 2 chistes más
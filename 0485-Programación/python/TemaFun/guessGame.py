import random

print("Bienvenidos al guessing game!")
print("Estoy pensando en un numero entre 1 y 20")

# Generate a random number
secret_number = random.randint(1, 20)

attempts = 0

while True:
    guess = input("Enter your guess: ")

    # TO DO: Comprobar que ha introducido un numero

    guess = int(guess)
    attempts += 1

    # si el guess es < secret_number, mostrar un mensaje: Demasiado pequeño
    # si el guess es > secret_number, mostrar un mensaje: Demasiado grande
    # si no, es correcto! y salir del juego


# -----------------------
# Actividad 2: Hacer otro juego pero esta vez con palabras
# words = ["apple", "banana", "cherry", "orange", "grape", "mango", "peach"]

# Shuffle the list
#random.shuffle(words)
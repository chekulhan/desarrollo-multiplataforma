import time

def move_object(symbol="🚀", steps=30, delay=0.05):
    for i in range(steps):
        line = " " * i + symbol
        print(f"\r{line}", end="")
        time.sleep(delay)

    print()  # move to next line at the end
    
move_object()


# Mejoras:
# ....🚀 agregar puntos despues
# Preguntar al usuario por el delay o velocidad y ajustar el programa

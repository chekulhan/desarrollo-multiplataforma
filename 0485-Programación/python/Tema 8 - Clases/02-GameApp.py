class Heroe:

    def __init__(self, nombre, posicion, vidas):
        self.nombre = nombre
        self.posicion = posicion
        self.vidas = vidas

    def check_collide(self, enemigo):
        if self.posicion == enemigo.posicion:
            self.vidas -=1
            print("Atacado")

    def move(self):
        self.posicion +=1   
    

class Enemigo:
    def __init__(self, nombre, posicion):
        self.nombre = nombre
        self.posicion = posicion

# --------------------------------------
# TAREA: Dado el juego de abajo, crear las clases de Heroe e Enimigo
# --------------------------------------

def main():
    e1 = Enemigo("dath vader", 3)
    e2 = Enemigo("joker", 5)
    e3 = Enemigo("freddy kruger", 6)

    enemigos = [e1, e2, e3]

    superman = Heroe("superman", 1, 3)

    for i in range(3): # numero de tornos
        for e in enemigos:
            superman.check_collide(e)

        superman.move()


if __name__ == "__main__":
    main()

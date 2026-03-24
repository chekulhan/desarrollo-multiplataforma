class Character:
    def __init__(self, nombre, posicion):
        self.nombre = nombre
        self.posicion = posicion

    def __str__(self):
        return f"Soy {self.nombre}"

    def move(self):
        self.posicion += 1

    # protected
    def _move_1(self):
        print("Im moving")

    # private con mangling
    def __move_1(self):
        print("Im moving __move_1")

    # print(e._move_1()) # disponible pero no deberia accederlo
    #print(e._Character__move_1()) # wrangling

class Hero(Character):

    def __init__(self, nombre, posicion, vidas):
        super().__init__(nombre, posicion)
        self.vidas = vidas

    def check_collide(self, enemigo):
        if self.posicion == enemigo.posicion:
            self.vidas -=1
            print(f"Atacado por {enemigo}")
            print(f"Ahora tengo {self.vidas} vidas")


    

class Enemy(Character):
    def __init__(self, nombre, posicion, pelicula):
        super().__init__(nombre, posicion)
        self.pelicula = pelicula
    

    def status(self):
        return f"Im an enemy at {self.posicion}"



def main():
    e1 = Enemy("darth vader", 3, "star wars")
    e2 = Enemy("joker", 5, "batman")
    e3 = Enemy("freddy kruger", 6, "freddy kruger")

    enemies = [e1, e2, e3]
        

    superman = Hero("superman", 1, 3)

    for i in range(3): # numero de tornos
        for e in enemies:
            superman.check_collide(e)

        superman.move()



if __name__ == "__main__":
    main()

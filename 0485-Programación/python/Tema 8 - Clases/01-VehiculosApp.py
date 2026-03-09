class Vehiculo:
    def __init__(self, marca, modelo,año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.velocidad = 0

    def mostrar_info(self):
        print(f"Tu vehiculo {self.marca}, {self.modelo} es del año {self.año}")

    def colision(self, otro_vehiculo):
        print("Accidente")
        otro_vehiculo.mostrar_info()
        self._velocidad = 0
        otro_vehiculo._velocidad = 0

class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, ruedas):
        super().__init__(marca, modelo, año)
        self.ruedas = ruedas
        
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Y tiene {self.ruedas} ruedas")

# TO DO
# Agregar una clase Coche



def main():
    v = Vehiculo("toyota", "rav4", 2015)
    v.mostrar_info()

    m = Moto("harley", "davidson", 1999, 2)
    m.mostrar_info()

    # accidente
    v.colision(m)

    # TO DO
    # agregar todos los vehiculos a una lista de vehiculos, y ejecutar un metodo, por ejemplo conducir()

if __name__ == "__main__":
    main()

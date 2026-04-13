

class Recipe_v1:
    _name = "" # atributo protected

    def __init__(self, name, ingredients):
        self._name = name
        self.ingredients = ingredients

    # crear nuestro propio print()
    def __str__(self):
        return f"Im a {self._name}"

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name



def main():
    x = Recipe_v1("carrots recipe", "carrots")
    print(x)
    x.setName("Carrot cake")
    print(x.getName())


if __name__ == "__main__":
    main()




# @property - Es un decorador - Cambia el comportamiento de un método (lo convierte en un atributo)
# anotaciones de tipos - name: str

class Recipe_v2:
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

"""
Otros decaoradores comúnes con clases son:

# @staticmethod

    @staticmethod
    def sumar(a: int, b: int) -> int:
        return a + b
        
    Método que no usa self - no hace falta pasar self ya que no hace uso sus atributos


# @dataclass  
    automatizar códifo como __init__, __str__, etc.. - boilerpoint code

from dataclasses import dataclass

@dataclass
class Persona:
    nombre: str
    edad: int

    
# @abstractmethod
    Oobliga que las clases hijos lo implementa

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self) -> None:
        pass
"""
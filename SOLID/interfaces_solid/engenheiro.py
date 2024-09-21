from typing import Type
from interface.formas import IFormas

class Engenheiro:

    def __init__(self, nome: str) -> None:
        self.nome = nome

    def medir_perimetro(self, terreno: Type[IFormas]):
        perimetro = terreno.get_perimetro()
        print('{} mediu o perimetro: {} m'.format(self.nome,perimetro))

    def medir_area(self, terreno: Type[IFormas]):
        area = terreno.get_area()
        print('{} mediu a area: {} m2'.format(self.nome,area))

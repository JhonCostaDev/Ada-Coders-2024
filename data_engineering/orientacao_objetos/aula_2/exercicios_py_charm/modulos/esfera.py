#### Exercício 5
#Uma Bola (incluir volume e área de superfície)
# area 4*pi*r**2
#volume = 4/3 pi r ** 3
from math import pi

class Esfera:
    def __init__(self, raio:float) -> None:
        self._raio = raio
        self.pi = pi

    @property
    def raio(self)->float:
        return self._raio

    def area(self):
        return 4 * pi * (self._raio ** 2)

    def volume(self):
        return 4/3 * pi * self._raio ** 3

    def __repr__(self) -> str:
        return f'Area da esfera: {4 * pi * (self._raio ** 2):.2f}\nVolume da esfera: {4/3 * pi * self._raio ** 3:.2f}'
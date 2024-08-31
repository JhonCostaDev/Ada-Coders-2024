class Retangulo:
    def __init__(self, base:float, altura:float)->None:
        self._base = base
        self._altura = altura
    @property
    def base(self):
        return self._base
    @property
    def altura(self):
        return self._altura

    def area(self) ->float:
        return self._base * self._altura

    def perimetro(self) -> float:
        return 2 * (self._base + self._altura)

    def __repr__(self):
        return f'Área: {self._base * self._altura}\nPerímetro: {2 * (self._base + self._altura)}'


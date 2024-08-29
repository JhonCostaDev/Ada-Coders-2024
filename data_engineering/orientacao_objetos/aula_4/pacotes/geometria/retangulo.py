class Retangulo:
    def __init__(self, base:float, altura:float) -> None:
        self._base = base 
        self._altura = altura
        
    def calcular_area(self) -> float:
        return self._base * self._altura
    
    def calcular_perimetro(self) -> float:
        return  (self._base + self._altura) * 2
    
    @property
    def base(self) -> float:
        return self._base
    
    @property
    def altura(self) -> float:
        return self._altura
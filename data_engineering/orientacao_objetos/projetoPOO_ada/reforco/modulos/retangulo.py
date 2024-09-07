class Retangulo:
    def __init__(self, base:int, altura: int) -> None:
        self._base = base
        self._altura = altura
        
    def area(self) -> int:
        return self._base * self._altura
    
    def perimetro(self) -> int:
        return 2 * self._base + 2 * self._altura
    
    # Getters
    @property
    def base(self)-> int:
        return self._base
    @property
    def altura(self) -> int:
        return self._altura
    
    # Setters
    @base.setter
    def base(self, update) -> None:
        self._base = update
    @altura.setter
    def altura(self, update)-> None:
        self._altura = update

# Objeto     
r1 = Retangulo(2, 5)
print(r1.perimetro())
    
#Um quadrado (incluir cálculo de área e perímetro)
#TODO: Aprimorar para exibir resultados acima de 100cm em metros
class Quadrado:
    def __init__(self, lado:float)->None:
        self.__lado = lado
    #getter
    @property
    def lado(self):
        return self.__lado

    #setter
    @lado.setter
    def lado(self, new_lado):
        self.__lado = new_lado

    def area(self):
        return self.__lado ** 2
    def perimetro(self):
        return  self.__lado * 4
    def __repr__(self):
        return f'O quadrado com {self.__lado}cm tem:\numa área de {self.__lado**2:.2f}cm\ne um perimetro de {self.__lado * 4:.2f}cm'
#TODO: melhorar lógica try/except e aplicar ao atributo ano
class Carro:
    """Classe para instanciar um Carro"""
    def __init__(self, marca:str, modelo:str, ano:int,cor:str,num_portas=2) ->None :
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
        self._cor = cor
        self._placa =''
        self._doc = ''
        self._num_portas = num_portas

    # Getters
    @property
    def marca(self) -> str:
        return self._marca
    @property
    def modelo(self)-> str:
        return self._modelo
    @property
    def ano(self):
        return self._ano
    @property
    def cor(self)-> str:
        return self._cor
    @property
    def placa(self):
        return self._placa
    @property
    def doc(self):
        return self._doc

    # Setters
    @cor.setter
    def cor(self, nova_cor):
        self._cor = nova_cor
    @placa.setter
    def placa(self, nova_placa):
        self._placa = nova_placa
    @doc.setter
    def doc(self, novo_doc):
        self._doc = novo_doc


    def __str__(self) -> str:
        return f'''
========RESUMO======== 
Marca: {self._marca}
Modelo: {self._modelo}
Ano-Fabricação: {self._ano}
Cor: {self._cor}
Placa: {self._placa}
Documento: {self._doc}
Quantidade de Portas: {self._num_portas}
====================== 
'''

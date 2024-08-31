class Carro:
    def __init__(self, marca:str, modelo:str, cor: str, num_portas=2) -> None:
        self._marca = marca
        self._modelo = modelo
        self._cor = cor
        self._num_portas = num_portas
        self._placa = ''
        self._doc = ''

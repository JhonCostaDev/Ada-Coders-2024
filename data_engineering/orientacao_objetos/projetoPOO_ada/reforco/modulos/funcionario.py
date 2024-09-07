class Funcionario:
    def __init__(self, nome:str, cargo:str, valor_hora_trabalhada:float) -> None:
        self._nome = nome
        self._cargo = cargo
        self._valor_hra_trabalhada = valor_hora_trabalhada
        self._horas_trabalhadas = 0
        self._salario = 0
        
    def registrar_hora_trabalhada(self):
        self._horas_trabalhadas += 1
        
    def calcular_salario(self):
        self._salario = self._horas_trabalhadas * self._valor_hra_trabalhada
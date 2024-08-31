# testar a classe Pessoa
from modulos.pessoa import Pessoa

pedro = Pessoa('Pedro Celestino', 42, 102.8, 1.77)
print(pedro)
pedro.peso = 95.8

print(pedro)
pedro.engordar()
pedro.envelhecer()
pedro.emagrecer()
print(pedro)
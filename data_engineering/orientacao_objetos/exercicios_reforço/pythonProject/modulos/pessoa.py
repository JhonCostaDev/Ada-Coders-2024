'''
Exercício 1
Classe Pessoa: Crie uma classe que modele uma pessoa:
    Atributos: nome, idade, peso e altura
    Métodos: Envelhercer, engordar, emagrecer, crescer.
Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela
menor que 21 anos, ela deve crescer 0,5 cm.
'''
#TODO: implementar método exercicios para alterar a taxa de emagrecimento.
class Pessoa:
    def __init__(self, nome:str, idade:int, peso:float, altura:float) -> None:
        self._nome = nome
        self._idade = idade
        self._peso = peso
        self._altura = altura

    def crescer(self):
        if self._idade < 21:
            self._altura += 0.5

    def envelhecer(self):
        if 0 < self._idade < 120:
            self._idade += 1

    def engordar(self):
        if self._idade < 10:
            self._peso += 0.5
        elif self._idade < 18:
            self._peso += 1
        else:
            self._peso += 2

    def emagrecer(self):
        if self._idade < 10:
            self._peso -= 0.5
        elif self._idade < 18:
            self._peso -= 1
        else:
            self._peso -= 2
        # getters
    @property
    def nome(self) -> str:
        return self._nome

    @property
    def idade(self) -> int:
        return self._idade

    @property
    def peso(self) -> float:
        return self._peso

    @property
    def altura(self) -> float:
        return self._altura

    @peso.setter
    def peso(self, novo_peso)->None:
        self._peso = novo_peso

    @altura.setter
    def altura(self, nova_altura) -> None:
        self._altura = nova_altura

    def __repr__(self) -> str:
        return f'''
===========CADASTRO===========
NOME: {self._nome}
IDADE: {self._idade}
PESO: {self._peso}
ALTURA: {self._altura}
==============================
'''


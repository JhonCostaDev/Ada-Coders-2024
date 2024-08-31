class Conta:
    """ Exercício 2
Classe Conta Corrente: Crie uma classe para implementar uma conta-corrente.
A classe deve possuir os seguintes atributos:
* número da conta,
* nome do correntista
*saldo.
Os métodos são os seguintes:
* alterarNome
* depósito
* saque;
No construtor, saldo é opcional, com valor default zero e os demais
atributos são obrigatórios.
    """
    def __init__(self, num_conta:str, nome:str, saldo=0.0) -> None:
        self._num_conta = num_conta
        self._nome = nome
        self._saldo = saldo

    def alterar_nome(self, novo_nome):
        self._nome = novo_nome

    def receber_valor_usuario(self) -> float:
        while True:
           entrada = input("Digite um valor:\n")
           try:
               valor = float(entrada)
               return valor
           except ValueError:
                print('Valor incorreto, Digite um número maior que zero.')

    def deposito(self):
        Goi@ba_verde5417
    @property
    def num_conta(self) -> str:
        return self._num_conta
    @property
    def nome(self) -> str :
        return self._nome
    @property
    def saldo(self)-> float:
        return self._saldo






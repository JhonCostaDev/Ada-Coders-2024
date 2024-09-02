

class Conta:
    def __init__(self, num_conta: str, cliente: str, saldo = 0.0) -> None:
        self._num_conta = num_conta
        self._cliente = cliente
        self._saldo = saldo

    # Métodos
    def verificar_valor(self) -> float:
        while True:
           entrada = input("Digite um valor:\n")
           try:
               valor = float(entrada)
               if valor <= 0:
                   raise ValueError('Valor incorreto, Digite um número maior que zero.')
               else:
                   return valor
           except ValueError:
                print('Valor incorreto, Digite um número maior que zero.')
    
    def deposito(self):
        valor = self.verificar_valor()
        self._saldo += valor
        print(f'Deposito no valor de R${valor} realizado com sucesso')

    def saque(self):
        valor = self.verificar_valor()
        print(f'Valor solicitado: R$ {valor}')

        tem_saldo = self._saldo > 0 and self._saldo > valor
        try:
            if tem_saldo:
                self._saldo -= valor
                print(f'Saque autorizado no valor R${valor}')
            else:
                raise ValueError ('Saldo insuficiente.')
        except ValueError as e:
            print(e)


    # Getters
    @property
    def num_conta(self) -> str:
        return self._num_conta

    @property
    def cliente(self)->str:
        return self._cliente

    @property
    def saldo(self) -> float:
        return self._saldo
    
    # Setters
    @cliente.setter
    def cliente(self, novo_nome):
        self._cliente = novo_nome

    #
    def __repr__(self) -> str:
        return f'''
Conta: {self._num_conta}
Cliente: {self._cliente}
Saldo: {self.saldo}
'''


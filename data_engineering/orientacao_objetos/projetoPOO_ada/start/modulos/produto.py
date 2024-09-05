class Produto:
    def __init__(self, nome, quantidade, valor):
        self._nome = nome
        self._quantidade = quantidade
        self._valor = valor

    def __repr__(self):
        return f"{self._nome}: {self._quantidade}| {self._valor}"
    #Getters
    @property
    def nome(self):
        return self._nome

    @property
    def quantidade(self):
        return self._quantidade

    @property
    def valor(self):
        return self._valor

    # Setters
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
    @quantidade
    def quantidade(self, nova_quantidade):
        self._quantidade = nova_quantidade
    @valor
    def valor(self, novo_valor):
        self._valor = novo_valor

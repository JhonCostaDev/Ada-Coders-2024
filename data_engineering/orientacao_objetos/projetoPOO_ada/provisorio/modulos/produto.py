class Produto:
    def __init__(self, nome:str, quantidade: int, valor:float) -> None:
        self._nome = nome
        self._quantidade = quantidade
        self._valor = valor

    # Getters ==========================================================
    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def quantidade(self) -> int:
        return self._quantidade
    
    @property
    def valor(self) -> float:
        return self._valor
    
    # Setters
    @nome.setter
    def nome(self, update_nome):
        self._nome = update_nome

    @valor.setter
    def valor(self, update_valor):
        self._valor = update_valor

    def __repr__(self) -> str:
        return f"""
Produto: {self._nome}
Quantidade: {self._quantidade}
Valor: {self._valor}
"""

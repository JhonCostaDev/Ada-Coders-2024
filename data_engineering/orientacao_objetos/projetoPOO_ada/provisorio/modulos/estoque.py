class Estoque:
    def __init__(self) -> None:
        self.estoque = {}
        self.quantidade_estoque = len(self.estoque)
    def exibir_estoque(self):
        
        if self.quantidade_estoque == 0:
            print('Estoque Vazio')
        else:
            for chave, valor in self.estoque.items():
                print(f'{chave} : {valor}')

    # def adicionar_item(self, produto):
    #     if produto == self.estoque
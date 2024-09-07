from produto import Produto
class Estoque:
    def __init__(self) -> None:
        self.estoque = {}
        self.quantidade_estoque = len(self.estoque)
        
    #TODO: ver sobre atributos estaticos
    def exibir_estoque(self):
        if self.quantidade_estoque == 0:
            print('Estoque Vazio')
        else:
            for chave, valor in self.estoque.items():
                print(f'{chave} : {valor}')

    def adicionar_item(self, produto):
        # for chave in self.estoque.keys():
        #     if chave == produto:
        #         chave.quantidade = valor
        nome = 
        quantidade = 
        valor =
        novo_item = Produto(nome, quantidade, valor)
        
            
                
                
                
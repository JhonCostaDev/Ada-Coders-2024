from start.modulos.produto import Produto


class Estoque:
    def __init__(self):
        self.produtos = {}

    def itens(self):
        if not self.produtos:
            print('O estoque está vazio')
        else:
            for produto in self.produtos.values():
                print(produto)

    def cadastrar_novo_item(self, nome, quantidade, valor):
        if nome in self.produtos:
            self.produtos[nome].quantidade += quantidade
            self.produtos[nome].valor += valor
        else:
            self.produtos[nome] = Produto(nome, quantidade, valor)
        print("Novo item cadastrado com sucesso.")

    def excluir_produto(self, nome):
        if nome in self.produtos:
            del self.produtos[nome]
            print(f"O produto {nome} foi excluído com sucesso.")
        else:
            print("produto nao cadastrado")

    def limpar_dados(self):
        self.produtos.clear()
        print("Estoque Limpo!")


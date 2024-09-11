import time
class Produto:
    def __init__(self, nome, valor) -> None:
        self._nome = nome
        self._valor = valor
    
    # Getters =======================================
    @property
    def nome(self)-> str:
        return self._nome
    
    @property
    def valor(self) -> float:
        return self._valor
    
    # Setters =======================================
    @nome.setter
    def nome(self, update_nome) -> None:
        self._nome = update_nome
        
    @valor.setter
    def valor(self, update_valor) -> None:
        self._valor = update_valor
        
        
##################################################################################################
class Estoque(Produto):
    # Dicionário populado para exibir as funcionalidades.
    estoque = {
        "caderno": [10, 7.99],  # [quantidade, preço unitário]
        "caneta": [28, 1.99],
        "borracha": [50, 2.55],
        "lápis": [50, 1.99]
    }
    
    # Método Contrutor da classe Estoque, ele herda atributos da classe Produto
    def __init__(self, nome, valor, quantidade) -> None:
        super().__init__(nome, valor)
        self._quantidade = quantidade
        self._valor_total_estoque = self.valor * self._quantidade
        
        # Condicional para verificar se um produto já está no dicionário, evitando perda de dados, já que dicionários não aceita chaves iguais.
        if self._nome not in Estoque.estoque:
            Estoque.estoque.update({self.nome: [ self._quantidade, self._valor]})
            print("==============================")
            print('Produto cadastrado com sucesso')
            print("==============================")
        else:
            print("==============================")
            print("     Produto já cadastrado    ")
            print("Se deseja atualizar/modificar um produto\nUtilize a opção ALTERAR!")
            print("==============================")
    
    # Método static utilizado para limpar o dicionário
    @staticmethod
    def limpar_estoque():
        Estoque.estoque.clear()
        print("==============================")
        print("      Estoque Limpo!!!")
        print("==============================")
    
    # Método static utilizado para excluir um par chave/valor do dicionário
    @staticmethod 
    def deletar_item(item):
        Estoque.estoque.pop(item)
        print("==============================")
        print("Operação realidada com sucesso")
        print("==============================")
        time.sleep(1.8)
    
    # Método static utilizado para exibir o pares chave/valor existentes no dicionário 
    @staticmethod   
    def exibir_estoque():
        
        if len(Estoque.estoque) == 0: # verifica se existem itens no dicionário
            print("===================================")
            print('Estoque Vazio, Cadastre novos itens')
            print("===================================")
            time.sleep(1.8)
        else:
       
            print("-" * 35)
            print(f"{'|Produto':<10}    |{'Quantidade':<10} |   {'Valor Unitário (R$)':<10}     |")
            print("-" * 35)
        
            # Linhas da tabela
            for chave, valor in Estoque.estoque.items():
                print(f"| {chave:<10}  | {valor[0]:<10}| R$ {valor[1]:<10}                |")
            
            input('\n\nPressione Enter para voltar para o menu principal\n')
    
    # Método static utilizado para alterar o nome de um produto no dicionário       
    @staticmethod
    def alterar_nome(nome, novo_nome):
        Estoque.estoque[novo_nome] = Estoque.estoque.pop(nome)
        print("==============================")
        print("Operação realidada com sucesso")
        print("==============================")
        time.sleep(2)
    
    # Método static utilizado para alterar o valor de um dicionário, ele utiliza a chave para buscar o item e alterar seu valor.    
    @staticmethod
    def alterar_valor(produto, novo_valor):
        Estoque.estoque[produto][1] = novo_valor
        print("==============================")
        print("Operação realidada com sucesso")
        print("==============================")
        time.sleep(1.8)
        
        
    # Método static utilizado para verificar a existência de um item no dicionário    
    @staticmethod
    def buscar_produto(produto) -> bool:
        if produto in Estoque.estoque:
            return True
        else:
            return False
        
        
        
        
        
        
        
        
    
    
    
    
    
        
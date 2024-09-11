import time
#TODO: separar classes e implementar criacao de estoque separados
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
        
        
####################################################################################################
class Estoque(Produto):
    banco = {}
    def __init__(self, nome, valor, quantidade) -> None:
        super().__init__(nome, valor)
        self._quantidade = quantidade
        self._valor_total_estoque = self.valor * self._quantidade
        if self._nome in Estoque.banco:
            print('Produto já cadastrado\nSe deseja atualizar nome ou valor, vá até o menu de produtos')
        else:
            Estoque.banco.update({self.nome: [self.nome, self._quantidade, self.valor, self._valor_total_estoque]})
    
    @staticmethod
    def limpar_estoque():
        Estoque.banco.clear()
        print("==============================")
        print("      Estoque Limpo!!!")
        print("==============================")
    @staticmethod 
    def deletar_iten(item):
        Estoque.banco.pop(item)
        print("==============================")
        print("Operação realidada com sucesso")
        print("==============================")
        
    @staticmethod   
    #TODO: usar static method para salvar em txt
    #TODO: Formatar saida deste metodo
    def exibir_estoque():
        if len(Estoque.banco) == 0:
            print('Estoque Vazio, Cadastre novos itens')
            time.sleep(2)
        else:
       
            print("-" * 35)
            print(f"{'|Produto':<10}  |{'Preço (R$)':<10} |{'Quantidade':<10} |")
            print("-" * 35)
        
            # Linhas da tabela
            for chave, valor in Estoque.banco.items():
                print(f"| {chave:<10}| {valor[1]:<10}| {valor[2]:<10}|")
            
            input('\n\nPressione Enter para voltar para o menu principal\n')
        
        
    
    
    
    
    
        
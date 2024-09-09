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
    estoque = {}
    def __init__(self, nome, valor, _quantidade) -> None:
        super().__init__(nome, valor)
        self._quantidade = _quantidade
        self._valor_total_estoque = self.valor * self._quantidade
        Estoque.estoque.update({self.nome: [self.nome, self._quantidade, self.valor, self._valor_total_estoque]})
    
    @staticmethod
    def limpar_estoque():
        Estoque.estoque.clear()
        print("==============================")
        print("      Estoque Limpo!!!")
        print("==============================")
    @staticmethod 
    def deletar_iten(item):
        Estoque.estoque.pop(item)
        print("==============================")
        print("Operação realidada com sucesso")
        print("==============================")
        
    @staticmethod   
    #TODO: usar static method para salvar em txt
    #TODO: Formatar saida deste metodo
    def exibir_estoque():
        if len(Estoque.estoque) == 0:
            print('Estoque Vazio, Cadastre novos itens')
        # print("Produto  |   Valor Unitário |    Quantidade  | Valor Total do Produto")  
        # for produto in Estoque.estoque.items():
        #     print(produto)
        # Cabeçalhos
        print("-" * 35)
        print(f"{'|Fruta':<10}  |{'Preço (R$)':<10} |{'Quantidade':<10} |")
        print("-" * 35)
    
        # Linhas da tabela
        for chave, valor in Estoque.estoque.items():
            print(f"| {chave:<10}| {valor[0]:<10}| {valor[1]:<10}|")
        
        
    
    
    
    
    
        
class Pessoa:

    # Construtor ==============================================
    def __init__(self, nome:str, idade:int, peso:float, altura:float) -> None:
        self._nome = nome
        self._idade = idade
        self._peso = peso
        self._altura = altura
       

    # Modulos ==============================================
    def crescer(self) ->None:
        if self._idade < 21:
            self._altura += 0.5

    # No método envelhecer, eu inseri uma variável com valor padrão False, onde os métodos engordar e emagrecer
    # serão acionador de acordo com a entrada dessa variável.
    def envelhecer(self, atividade_fisica=False) ->None:
        self._idade += 1
        self.crescer()
        if atividade_fisica:
            self.emagrecer()
        else:
            self.engordar() 
        
    def engordar(self) ->None:
        if self._peso < 200: 
            self._peso += 2
        
    def emagrecer(self) ->None:
        if self._peso > 35:
            self._peso -= 1.5

    #Getters ==============================================
    @property
    def nome(self)->str:
        return self._nome
    
    @property
    def idade(self)->int:
        return self._idade
    
    @property
    def peso(self)->float:
        return self._peso
    
    @property
    def altura(self)->float:
        return self._altura
    
    #Setters ==============================================
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @idade.setter
    def idade(self, nova_idade)->None:
        self._idade = nova_idade

    @peso.setter
    def peso(self, novo_peso):
        self._peso = novo_peso

    @altura.setter
    def altura(self, nova_altura)->None:
        self._altura = nova_altura

    # Método mágico para resumo de informações
    def __repr__(self) -> str:
        return f'''
Nome: {self._nome}
Idade: {self._idade}
Peso: {self._peso}
Altura: {self._altura}

'''



class Pessoa:
    def __init__(self, nome:str, idade:int, peso:float, altura:float) -> None:
        self._nome = nome
        self._idade = idade
        self._peso = peso
        self._altura = altura
        self._atividade_fisica = False

    # Modulos ==============================================
    def crescer(self) ->None:
        if self._idade < 21:
            self._altura += 0.5
    
    def envelhecer(self, atividade_fisica=False) ->None:
        self._idade += 1
        self.crescer()
        if atividade_fisica:
            self.emagrecer()
        else:
            self.engordar() 
        

    def engordar(self) ->None:
        self._peso += 2
        

    def emagrecer(self) ->None:
        self._peso -= 1.5
    
    def atividade_fisica(self):
        self._atividade_fisica = True


    #getters ==============================================
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

    @idade.setter
    def update_idade(self, nova_idade)->None:
        self._idade = nova_idade

    @altura.setter
    def update_altura(self, nova_altura)->None:
        self._altura = nova_altura

    def __repr__(self) -> str:
        return f'''
Nome: {self._nome}
Idade: {self._idade}
Peso: {self._peso}
Altura: {self._altura}
Atividade Fisica: {self._atividade_fisica}
'''



class Tamagushi:
    def __init__(self, nome:str) -> None:
        self._nome = nome
        self._fome = 2
        self._saude = 2
        self._idade = 0

    # TODO: Desenvolver a logica para o metodo humor
    def humor(self):
        # Como calcular humor
        # alto
        # normal
        # baixo
        if self._saude > 2 and self._fome < 3:
            return 'alto'
        elif self._saude > 2 and self._fome < 3:
            return 'alto'
        else:
            return 'alto'
    #Getters
    
    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def fome(self) :
        return self._fome
    
    @property
    def saude(self):
        return self._saude
    
    @property
    def idade(self):
        return self._idade
    
    # Setters
    #TODO: Melhorar nomes dos setters
    @nome.setter
    def alterar_nome(self, novo_nome):
        self._nome = novo_nome

    @fome.setter
    def update_fome(self, nova_fome):
        self._fome = nova_fome

    @saude.setter
    def update_saude(self, nova_saude):
        self._saude = nova_saude
    
    @idade.setter
    def update_idade(self, nova_idade):
        self._idade = nova_idade
class Tamagushi:
    def __init__(self, nome:str) -> None:
        self._nome = nome
        self._idade = 0
        # Os atributos abaixo serão classificados em uma escala de 0 à 5. Sendo 0 ruím, 3 normal e 5 bom.
        # Serão iniciados com o valor 2
        self._fome = 2
        self._saude = 2


    # Para calcular o humor do Tamagushi eu usei a média simples dos dois atributos e classifiquei o humor de
    # acordo com o resultado.
    def humor(self):
        humor = (self._fome + self._saude) / 2
        if humor <= 2:
            return 'Ruim'
        elif humor <= 3.5:
            return 'Normal'
        else:
            return 'Bom'

    # Sei que não foi pedido, mas criei esses métodos para modificar os atributos que determinarão o humor do Tamagushi.
    # Atividades que mudarão os atributos do Tamagushi
    # a variável (atributos_válidos) controlará o range dos atributos para que não ultrapassem  os limites.
    def comer(self):
        atributos_validos = self._saude and self._fome  >= 0 and self._saude and self._fome  <= 5
        if atributos_validos:
            self._fome += 0.8
            self._saude += 0.5

    def dormir(self):
        atributos_validos = self._saude and self._fome  >= 0 and self._saude and self._fome  <= 5
        if atributos_validos:
            self._fome -= 1
            self._saude += 0.8

    def brincar(self):
        atributos_validos = self._saude and self._fome  >= 0 and self._saude and self._fome  <= 5
        if atributos_validos:
            self._fome -= 1
            self._saude += 0.5

    def exercitar(self):
        atributos_validos = self._saude and self._fome  >= 0 and self._saude and self._fome  <= 5
        if atributos_validos:
            self._fome -= 1.2
            self._saude += 1.2


    #Getters =======================================================
    
    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def fome(self) -> int:
        return self._fome
    
    @property
    def saude(self) -> int:
        return self._saude
    
    @property
    def idade(self) -> int:
        return self._idade
    
    # Setters =======================================================
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @fome.setter
    def fome(self, nova_fome):
        self._fome = nova_fome

    @saude.setter
    def saude(self, nova_saude):
        self._saude = nova_saude
    
    @idade.setter
    def idade(self, nova_idade):
        self._idade = nova_idade

    # == == == == == == == == == == == == == == == == == == == == == == == == == == == =
    def __repr__(self):
        return f'''
        Nome: {self._nome}
        Humor: {self.humor()}
        Fome: {self._fome}
        Saúde: {self._saude}
        '''
class Cliente:
    def __init__(self, nome: str, idade: str, email:str) -> None:
        self._nome = nome
        self._idade = idade
        self._email = email
        
    def exibir_informacoes(self):
        print(f'''
Nome: {self._nome}
Idade: {self._idade}
E-mail: {self._email}
            ''')
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade
    
    @property
    def email(self):
        return self._email
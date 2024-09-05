class Hello:
    def __init__(self):
        self._nome = self.get_name()

    def get_name(self):
        user = input('Qual seu nome:\n')
        return user
    def saudacao(self):
        return f'Bem-vindo {self._nome}'
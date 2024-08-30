'''
exercicio 8 aula 2 POO

Com base no exercício anterior, crie um sistema de cadastro com dicionários e a classe Cliente; 

* Cada cliente deve ter como chave o seu CPF. 
Seu programa deve perguntar se o usuário quer cadastrar um novo cliente, alterar um cadastro ou sair.
Obs.: tente fazer esse exercício pode criando uma classe Sistema, que irá controlar o sistema de cadastros. 

* Essa classe deve ter o atributo cadastro e os métodos para imprimir os cadastrados, cadastrar um novo, alterar um cadastro ou sair.'''
#%%
from pacotes.cliente import Cliente

# def menu():
#     opcao = input('''

#                   ''')

clientes = []

# claudio = Cliente('Claudio', 22, 'claudio@email.com')
# claudio.exibir_informacoes()
def novo_cliente():
    dicionario = dict()
    cpf = '987.987.321.45'#input('Digite o CPF:\n')
    nome = 'Maria joana'#input('Digite o nome completo:\n')
    idade = 65#int(input('Digite sua idade:\n'))
    email = 'maria.joana@email.com'#input('Digite seu e-mail:\n')
    cliente = Cliente(nome, idade, email)
    
    dicionario.update({cpf: cliente})
    return dicionario
    
c1 = novo_cliente()

info = c1
    
    
print(info)


# %%

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'Pessoa(nome={self.nome}, idade={self.idade})'

# Criando uma instância da classe Pessoa
pessoa = Pessoa("João", 30)

# Exibindo os atributos
print(pessoa)

# %%

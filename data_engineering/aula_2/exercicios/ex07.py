'''7) Faça um código para criar uma agenda telefônica. 

O programa deve armazenar o nome e um ou mais telefones do contato. 

Em seguida, o usuário vai informar o nome de algum contato armazenado e o programa deve retornar os número(s) do contato caso queira pode utilizar o método .split()
contatos = {
    "Alice": "1234-5678",
    "Bob": "2345-6789",
    "Carlos": "3456-7890",
    "Diana": "4567-8901",
    "Eva": "5678-9012"
}
'''
contatos = { #para testes
    "Alice": "1234-5678",
    "Bob": ["2345-6789", "2345-6789", "2345-6789", "2345-6789"],
    "Carlos": "3456-7890",
    "Diana": "4567-8901",
    "Eva": "5678-9012"
}
#=========================================================================
agenda = {}
print("==== AGENDA TELEFÔNICA ====")

def menu():
   
    menu = input('''
Escolha uma das opções abaixo:
1 - Salvar Novo Contato
2 - Buscar Contato
3 - Exibir Todos os Contatos Salvos
0 - SAIR   
''')
    return int(menu)
def salvar_contato():
    
    telefones = []
    nome = input("Digite o Nome para o novo Contato:\n").lower()    
    while True:
        telefone = input(f"Digite o número do contato {nome}\n")
        telefones.append(telefone)
        print(f"Deseja salvar outro número de telefone para o contato {nome}?")
        novo_telefone = int(input('''Digite
                              1 - sim  
                              2 - não
                              '''))
        if novo_telefone == 2:
            break
    return nome, telefones

def buscar_contato(dicionario, nome):
    print(dicionario.get(nome))

def exibir_contatos(dicionario):
    for chave, valor in dicionario.items():
        print(f" Nome: {chave} - {valor}")



opcao = menu();
while opcao != 0:
    if opcao == 1:
        chave, valor = salvar_contato()
        contatos.update({chave : valor})
    
    if opcao == 2:
        buscar = input("Digite o nome do contato:\n")#.lower()
        buscar_contato(contatos, buscar)
    
    if opcao == 3:
        exibir_contatos(contatos)
    
    opcao = menu()

print('fim')

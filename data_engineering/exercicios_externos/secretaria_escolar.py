def menu():
    print('''
          SECRETARIA ESCOLAR
          DIGITE:
          
          1 - CADASTRAR NOTAS
          2 - VISUALIZAR NOTAS
          0 - SAIR
          ''')
    opcao = int(input('Digite uma das opções:'))
    return opcao
def salvar_notas():
    lista = []
    
    lista.append(input("Digite o nome do aluno:\n"))
    for i in range(4):
        lista.append(float(input(f"Digita a {i + 1}º nota")))
        
    return lista
menu()
# for i in range(5):
#     notas_aluno.append(salvar_notas())
# print(notas_aluno)
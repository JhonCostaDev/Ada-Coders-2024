# notas = (
#     'jhon', (1, 2, 3, 4),'josy', (1, 2, 'goiaba', 4),'Victor', (1, 2, 3, 4)
#     )
# #print(notas[3][2])

# notas = [["jhon", 1, 2, 3 ,4]]


alunos_teste = [
    ["Ana", (8.5, 7.0, 9.0, 6.5)],
    ["Bruno", (4.5, 8.0, 6.0, 7.0)],
    ["Carla", (9.0, 8.5, 7.5, 8.0)],
    ["Daniel", (6.5, 7.0, 8.0, 7.5)],
    ["Eduarda", (8.0, 9.0, 7.0, 8.5)],
    ["Felipe", (4.0, 6.5, 4.5, 5.5)],
    ["Gabriela", (9.5, 8.0, 7.0, 8.5)],
    ["Henrique", (6.0, 7.5, 8.0, 7.0)],
    ["Isabela", (3.5, 6.6, 7.5, 3.0)],
    ["João", (7.0, 6.0, 8.0, 7.5)]
]


# def calcula_media(lista):
#     notas_aluno = []
#     for indice, aluno in enumerate(lista):
#         aluno = lista[indice][0]
#         notas = lista[indice][1]
#         media = sum(notas) / len(notas)
#         resultado = (aluno, media)
#         notas_aluno.append(resultado)
#     return notas_aluno
# resultado = calcula_media(alunos_teste)

# print(resultado)
#print(alunos_teste[-1][0])

#=========================================
notas = []

        
def salvar_notas():
    lista = []
    
    notas = []
    lista.append(input("Digite o nome do aluno:\n"))
    for i in range(4):
        notas.append((float(input(f"Digita a {i + 1}º nota\n"))))
    
    tupla = tuple(notas)
    lista.append(tupla)a
               
    return lista

print("Secretaria escolar\n")
while True:
    notas.append(salvar_notas())
    opcao = int(input("Deseja salvar notas para um aluno? (1 - SIM / 2 - NÃO)\n"))
    if opcao != 1:
        break

print(notas)
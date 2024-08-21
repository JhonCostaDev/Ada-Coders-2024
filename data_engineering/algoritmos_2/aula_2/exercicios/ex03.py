'''3) Faça uma função que conte quantas vezes cada elemento aparece em uma lista. Essa função deverá guardar os dados em um dicionário no qual as chaves são os elementos inseridos e os valores são a contagem de quantas vezes esse elemento aparece. ex de output: {"banana":2, "maçã":1}'''

def conta_itens(lista):
    dicionario = {}
    for item in lista:
        ocorrencias = lista.count(item)
        dicionario[item] = ocorrencias 
    return dicionario 

alunos = ['maria', 'rose', 'pedro', 'maria', 'antonia', 'maria', 'rose', 'luiza', 'pedro', 'francisco']

resultado = conta_itens(alunos)

for chave, valor in resultado.items():
    print(f'O aluno {chave} aparece em {valor} vezes na lista.')
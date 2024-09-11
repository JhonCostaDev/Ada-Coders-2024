''' criando o arquivo / quando nao existe
arquivo = open('teste.txt', 'x', encoding='UTF-8')
arquivo.write('banana, 50, 2.99\n')
arquivo.write('iogurte, 23, 4.99\n')
arquivo.write('uva, 150, 8.99\n')
arquivo.write('biscoito, 10, 4.99\n')

arquivo.close()
'''
def ler_arquivo(arquivo):
    with open(arquivo, 'r', encoding='UTF-8') as file:
        linhas = file.readlines() # readlines com s no final
        produtos = [linha.strip().split(',') for linha in linhas]
    return produtos
lista = ler_arquivo('frutas.txt')
print(lista)
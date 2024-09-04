# Função para ler o arquivo e armazenar os dados em uma lista
def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    produtos = [linha.strip().split(',') for linha in linhas]
    return produtos

# Função para modificar os valores dos produtos
def modificar_valores(produtos, fator):
    for produto in produtos:
        produto[2] = str(float(produto[2]) * fator)  # Multiplica o valor pelo fator
    return produtos

# Função para escrever os dados de volta no arquivo
def escrever_arquivo(nome_arquivo, produtos):
    with open(nome_arquivo, 'w') as arquivo:
        for produto in produtos:
            arquivo.write(','.join(produto) + '\n')
'''
# Nome do arquivo
nome_arquivo = 'teste.txt'

# Ler o arquivo
produtos = ler_arquivo(nome_arquivo)

# Modificar os valores (por exemplo, aumentar os valores em 10%)
fator = 1.10
produtos_modificados = modificar_valores(produtos, fator)

# Escrever os dados de volta no arquivo
escrever_arquivo(nome_arquivo, produtos_modificados)

print("Valores dos produtos atualizados com sucesso!")
'''
lista = ler_arquivo('teste.txt')
for i in lista:
    print(i)
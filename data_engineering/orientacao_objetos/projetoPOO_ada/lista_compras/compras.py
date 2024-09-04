
# pegar o arquivo na pasta
arquivo = open('lista compras.txt', 'r', encoding='UTF-8')
# atribuir a uma variavel
conteudo = arquivo.read()
# transformo o arquivo em uma lista
lista = conteudo.splitlines()

# crio um dicionario vazio
estoque = {}

# crio uma lista com o cabeçalho da tabela
cabecalho = lista[0].split(',')

# iteracao para construção do dicionário onde a chave é o nome do item e o valor é uma
# tupla (quantidade, valor)
for i in lista:
    # essa condicional é para não adicionar ao dicionário os itens do cabeçalho
    if i.split(',') == cabecalho :
        continue
    # construção do dicionário
    else:
        produto = i.split(',')
        estoque.update({produto[0]: (produto[1], produto[2])})
        #print(produto)


print(estoque)
#TODO: exibir uma tabela no terminal com os itens do estoque

#TODO: Começar a construir a classe



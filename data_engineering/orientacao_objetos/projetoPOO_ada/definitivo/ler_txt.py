def ler(arquivo_txt):
    dic = {}
    with open(arquivo_txt, 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            conteudo = linha.strip().split('\n')
            chave, valor = conteudo[0], 
            return chave, valor
    # return dic
    # return linhas


a = ler('frutas.txt')
print(a)
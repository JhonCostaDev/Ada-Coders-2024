'''6) Faça um código contador de palavras. O usuário vai inserir um texto qualquer e o programa vai contar a quantidade de cada palavra no texto, armazenando o resultado em um dicionário e exibindo o resultado para o usuário.

caso queira pode utilizar o .split() e .replace()
'''
#TODO: quantidade de ocorrencias daquela palavra.

def contador_palavras(frase):
    dicionario = {}
    lista = frase.split()
    quantidade_palavras = len(lista)
    
    for item in lista:
        if item != '-':
             if item[-1] == '.' or ',' or '?' or '!':
                nova_palavra = item.replace(".", "")
                dicionario.update({nova_palavra : len(item)})
            #dicionario[item] = len(item)
    return dicionario


frase_1 = 'Não importa o quão devagar você vá, desde que você não pare. - Confúcio'

frase_2 = 'Na minha terra tem palmeiras onde canta o sabiá.'
resultado = contador_palavras(frase_2)

for chave, valor in resultado.items():
    print(f'A palavra ({chave}) tem {valor} letras')


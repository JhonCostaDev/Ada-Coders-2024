'''Crie uma lista qualquer e faça um programa que imprima cada elemento da lista usando o for'''

frutas = ['maçã', 'banana', 'goiaba', 'melão', 'maracujá', 'tomate', 'melância', 'pera', 'uva']

# for com range / len

for indice in range(len(frutas)):
    print(frutas[indice], end=" ,")
print("-"*40)
# for in 

for fruta in frutas:
    print(fruta, end=" ,")
    
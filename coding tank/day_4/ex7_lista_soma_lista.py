''' 7 - Faça um programa que dada duas listas de mesmo tamanho, crie uma nova lista com cada elemento igual a soma dos elementos da lista 1 com a lista 2, na mesma posição.
'''
Lista_a =[ 37, 12, 5, 23, 48, 19, 9, 41, 30, 14 ]

Lista_b=[ 3, 47, 26, 38, 7, 50, 34, 21, 2, 40 ]

lista_soma = []

if len(Lista_a) == len(Lista_b):
    for i in range(len(Lista_a)):
        lista_soma.append(Lista_a[i] + Lista_b[i])
        
for item in lista_soma:
    print(item, end=", ")
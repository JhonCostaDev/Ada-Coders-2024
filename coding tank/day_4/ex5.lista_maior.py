'''5 - Faça um programa que imprima o maior número de uma lista, sem usar o método/função max()
'''

lista = [ 37, 12, 5, 23, 48, 19, 9, 41, 30, 14, 3, 47, 26, 38, 7, 50, 34, 21, 2, 40, 16, 28, 11, 44, 6, 33, 49, 24, 8, 36, 18, 1, 39, 25, 10, 45, 20, 4, 29, 15, 46, 22, 13, 35, 27, 43, 17, 31, 32]

maior = lista[0]
for item in lista:
    if item > maior:
        maior = item
        
print(f"O maior item da lista é: {maior}")
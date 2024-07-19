'''
Faça um programa que olhe todos os items de uma lista e diga quantos deles são pares.
'''

lista = [ 37, 12, 5, 23, 48, 19, 9, 41, 30, 14, 3, 47, 26, 38, 7, 50, 34, 21, 2, 40, 16, 28, 11, 44, 6, 33, 49, 24, 8, 36, 18, 1, 39, 25, 10, 45, 20, 4, 29, 15, 46, 22, 13, 35, 27, 43, 17, 31, 32]

itens_pares = 0
pares = []

for item in lista:
    if item % 2 == 0:
        itens_pares +=1
        pares.append(item)

print(f"Existem {itens_pares} na lista")
print("Sendo eles: ")   
for item in pares:
    print(item, end=" ")



print("Itens pares ordenados")
print(sorted(pares))
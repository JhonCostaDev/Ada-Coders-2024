'''6 - Agora usando a função max(), faça um programa que imprima os três maiores números de uma lista.
'''

lista = [ 37, 12, 5, 23, 48, 19, 9, 41, 30, 14, 3, 47, 26, 38, 7, 50, 34, 21, 2, 40, 16, 28, 11, 44, 6, 33, 49, 24, 8, 36, 18, 1, 39, 25, 10, 45, 20, 4, 29, 15, 46, 22, 13, 35, 27, 43, 17, 31, 32]

maiores = []
i = 0
while i < 3:
    maiores.append(max(lista))
    lista.remove(max(lista))
    i += 1
print("Os três maiores itens da lista são: ", end="")
for item in maiores:
    print(item, end=" ")
    
print("")
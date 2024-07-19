'''8. Faça um programa que dadas duas listas de mesmo tamanho, imprima o produto escalar entre elas.
'''

lista_a =[ 37, 12, 5, 23, 48, 19, 9, 41, 30, 14 ]

lista_b=[ 3, 47, 26, 38, 7, 50, 34, 21, 2, 40 ]

soma = 0

for item in range(len(lista_a)):
    soma += lista_a[item] * lista_b[item]
    
print(f"O produto escalar das duas listas é: {soma}") 

a = [1, 2, 3]
b = [3, 2, 1]
soma2 = 0
for item in range(len(a)):
    soma2 += a[item] * b[item]
    
print(f"O produto escalar das duas listas é: {soma2}")

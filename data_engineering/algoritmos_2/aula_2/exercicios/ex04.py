'''4) Faça um código que receba múltiplos números inteiros em seguida informe quantos são pares e quantos são ímpares.
'''
numeros = (42, 17, 93, 58, 21, 76, 34, 89, 12, 67, 55, 3, 81, 29, 64, 48, 7, 99, 23, 50, 2)

par = 0

for numero in numeros:
    if numero % 2 == 0:
        par += 1
    
impar = len(numeros) - par
print(f'Exitem {par} numeros pares e {impar} números ímpares.')

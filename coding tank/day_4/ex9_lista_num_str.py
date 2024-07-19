'''9 - Faça um programa que pede para o usuário digitar 5 números e ao final, imprimir uma listas com os 5 números digitados pelo usuário (sem converter os números para int ou float)
'''
numeros = []
for i in range(5):
    numeros.append(input(f"Digite o {i + 1}º número :\n"))

print("Os números digitados foram: ")
for numero in numeros:
    print(numero, end=" ")
    
print(numeros)
    

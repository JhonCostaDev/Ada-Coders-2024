'''3 - Faça um programa que peça para o usuário digitar um número n e imprima uma lista com todos os números de 0 a n -1'''

n = int(input("Digite um número inteiro\n"))

for i in range(n):
    print(i, end=" ,")
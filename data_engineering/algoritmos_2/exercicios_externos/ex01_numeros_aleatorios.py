import random
'''
01 - Make a program that gets a list of five integers numbers and display them. /Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
'''
# Gerar números
numbers = []
for number in range(5):
   numbers.append(random.randrange(1, 100))
    
# Ler o vetor
for number in numbers:
   print(number)
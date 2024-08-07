import random
'''
Make a program that reads a list of ten reals numbers and display them in reverse order.
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
'''
numbers = []
# Generate random numbers / Gerar os números aleatórios  
for number in range(10):
   numbers.append(float(random.randrange(1, 100)))

# Display the list of index and numbers using the enumerate function / Exibir a lista de indices e números usando a função enumerates. 
for index, number in enumerate(numbers):
    print(f"position: {index + 1} - Number: {number}")
 
# Display reverse order of the list of numbers using the loop while / Exibir a lista na ordem inversa 
print("\n========= Reverse =========")
i = len(numbers) - 1
while i >= 0:
    print(f"position: {i + 1} - Number: {numbers[i]}")
    i -= 1
    
    
   
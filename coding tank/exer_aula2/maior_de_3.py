'''
9) Faça um programa que leia três números e mostre o maior deles.
a, b, c

a -> b
a -> c
b -> c
'''
print("Maior de três números:\n")

numero_1 = int(input("Digite o primeiro número: \n"))
numero_2 = int(input("Digite o segundo número: \n"))
numero_3 = int(input("Digite o terceiro número: \n"))


if numero_1 > numero_2 and numero_1 > numero_3:
    print(f"O número {numero_1} é o maior!")
elif numero_2 > numero_1 and numero_2 > numero_3:
    print(f"O número {numero_2} é o maior!")
else: 
    print(f"O número {numero_3} é o maior!")
'''1 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
minha formula
C = (F - 32) / 1.8
F = C * 1.8 + 32
'''
fahrenheit = float(input("Digite a temperatura em  Fahrenheit: \n"))

celcius = (fahrenheit - 32) / 1.8

print(f"{fahrenheit}º Fahrenheit, correspondem à : {celcius}º Celsius.")

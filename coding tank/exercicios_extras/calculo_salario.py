'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

'''
salario_hora = float(input("Digite seu salário / hora: \n"))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas: \n"))

salario_mensal = salario_hora * horas_trabalhadas

print(f"Total mensal: {salario_mensal}")
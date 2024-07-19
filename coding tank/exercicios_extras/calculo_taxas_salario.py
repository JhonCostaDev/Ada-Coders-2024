'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 

Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''
ir = 0.11
inss = 0.8
sindicato = 0.05

salario_hora = float(input("Digite seu salário / hora: \n"))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas: \n"))

salario_mensal = salario_hora * horas_trabalhadas

ir = salario_mensal * 0.11
inss = salario_mensal * 0.08
sindicato = salario_mensal * 0.05

salario_liquido = salario_mensal - ir - inss - sindicato

print(f"Salário Bruto: R${salario_mensal}\nIR: R${ir}\nINSS: R${inss}\nSINDICATO: R${sindicato}")
print(f"Salário Líquido: R${salario_liquido}")
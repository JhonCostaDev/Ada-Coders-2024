'''
5) Escreva um programa que peça a nota de 3 provas de um aluno e verifique se ele passou ou não de ano.
Obs.: O aluno irá passar de ano se sua média for maior que 6.
'''
print("=====MÉDIA NOTAS======")

nota_1 = float(input("Digite a primeira nota:\n"))

nota_2 = float(input("Digite a segunda nota:\n"))

nota_3 = float(input("Digite a terceira nota:\n"))

media = (nota_1 + nota_2 + nota_3) / 3

if media > 6:
	print("Aprovado")
else:
	print("Reprovado")
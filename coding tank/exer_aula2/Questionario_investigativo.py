'''
7) Vamos fazer um programa para verificar quem é o assassino de um crime. Para descobrir o assassino, 
a polícia faz um pequeno questionário com 5 perguntas 
onde a resposta só pode ser sim ou não:

a. Mora perto da vítima?

b. Já trabalhou com a vítima?

c. Telefonou para a vítima?

d. Esteve no local do crime?

e. Devia para a vítima?

Cada resposta sim dá um ponto para o suspeito. A polícia considera que os suspeitos com 5 pontos são os assassinos, com 4 a 3 pontos 
são cúmplices e 2 pontos são apenas suspeitos, necessitando outras investigações. Valores iguais ou abaixo de 1 são liberados.
'''


print("Questionário Investigativo\nResponda as peguntas abaixo digitando 0 para Nao e 1 para Sim\n")

mora_perto = int(input("Mora perto da vítima?\n"))

ja_trabalhou = int(input("Já trabalhou com a vítima?\n"))

telefonou = int(input("Telefonou para a vítima?\n"))

esteve_no_local = int(input("Já esteve no local do crime?\n"))

devia = int(input("Devia para a vítima?\n"))

pontos = 0

if mora_perto == 1:
	pontos += 1
	
if ja_trabalhou == 1:
	pontos += 1
	
if telefonou == 1:
	pontos += 1
	
if esteve_no_local == 1:
	pontos += 1
	
if devia == 1:
	pontos += 1
	
#print(pontos)
if pontos == 5:
	print("Assassino!")
elif pontos ==4 or pontos == 3:
	print("Cúmplice")
elif pontos == 2:
	print("Suspeito!")
else:
	print("Liberado!")
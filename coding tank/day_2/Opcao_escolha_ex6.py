'''6) Faça um programa que mostre uma questão de múltipla escolha com 5 opções (letras a, b, c, d, e). 
Sabendo a resposta certa, o programa deve receber a opção do usuário e informar a letra que o usuário marcou e se a resposta está certa ou errada.
'''
print("MULTIPLA ESCOLHA")

print("Oito alunos de uma turma da Ada, entre eles Anderson e Bento,  estão em uma fila. Qual das opcões abaixo representa a probabilidade de os dois estarem juntos na fila, em qualquer ordem?\na)30%\nb)12,5%\nc)40%\nd)25%\ne)20%")
print("\n")
resposta = input("Digite sua opcao: \n")
'''
if resposta.upper() == "A":
	print("Resposta errada")
elif resposta.upper() == "B":
	print("Resposta errada")
elif resposta.upper() == "C":
	print("Resposta errada")
elif resposta.upper() == "D":
	print("Resposta Correta!")
elif resposta.upper() == "E":
	print("Resposta errada")
else:
	print("Opcao inválida...")
 '''
 
if resposta.upper() != 'D':
    print("Resposta errada")
else:
    print("Resposta Correta!")
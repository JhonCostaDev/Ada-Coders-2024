# Crie um algoritmo que calcule o IMC (índice de massa corporal). O IMC é calculado com a formula PESO/(ALTURA ^ 2). Para isso, coloque as informações nas variáveis e ao final apresente o resultado como no exemplo: "O IMC é 18"

print("====== CÁLCULO IMC ======")

altura = float(input("Digite sua altura:\n"))
peso =  float(input("Digite seu peso: \n"))

imc = peso / altura ** 2

print(f"Seu IMC é de: {imc}")

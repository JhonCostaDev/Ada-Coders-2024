'''
8) Um produto vai sofrer aumento de acordo com a Tabela 1 abaixo. Faça um programa que peça para o usuário digitar o valor do produto de acordo 
com o preço antigo e escreva uma das mensagens da Tabela 2, de acordo com o preço reajustado:

Tabela 1

| Preço Antigo         | % de aumento |
|----------------------|--------------|
| Até 50 reais         | 5%           |
| Entre 50 e 100 reais | 10%          |
| De 100 a 150 reais   | 13%          |
| Acima de 150 reais   | 15%          |
Tabela 2

| Preço Novo            | Mensagem   |
|-----------------------|------------|
| Até 80 reais          | Barato     |
| Entre 80 e 115 reais  | Razoável   |
| Entre 115 e 150 reais | Normal     |
| Entre 150 e 170 reais | Caro       |
| Acima de 170 reais    | Muito Caro |
'''
print("Ajuste de preco".upper())

produto = float(input("Digite o valor do produto: \n"))
valor_atualizado = 0
if produto <= 50.0:
	valor_atualizado = produto + (produto * 0.05)
	#print("0.05")
elif produto <= 100:
	valor_atualizado = produto + (produto * 0.1)
	#print("0.1")
elif produto <= 150:
	valor_atualizado = produto + (produto * 0.13)
	#print("0.13")
else:
	valor_atualizado = produto + (produto * 0.15)
	#print("0.15")
	
if valor_atualizado <= 80.0:
	print(f"Novo preco: R${ valor_atualizado}\nBarato")
elif valor_atualizado <= 115.0:
	print(f"Novo preco: R${ valor_atualizado}\nRazoável")
elif valor_atualizado <= 150:
	print(f"Novo preco: R${ valor_atualizado}\nNormal")
elif valor_atualizado <= 170:
	print(f"Novo preco: R${ valor_atualizado}\nCaro")
else:
	print(f"Novo preco: R${ valor_atualizado}\nMuito Caro") 
''' Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    * o produto do dobro do primeiro com metade do segundo .
    * a soma do triplo do primeiro com o terceiro.
    * o terceiro elevado ao cubo.
'''
numeros = []
for i in range(3):
    if i <= 1:
        numeros.append(int(input("Digite um número inteiro: \n")))
    else:
        numeros.append(float(input("Digite um número real: \n")))

produto_dobro = (numeros[0] ** 2) * (numeros[1] / 2)
soma_triplo = (numeros[0] * 3) + numeros[2]
cubo = numeros[2] ** 3

print(f'''
      Produto do dobro: {produto_dobro}
      soma do triplo: {soma_triplo}
      Elevado ao cubo: {cubo}
      ''') 
''' 11 - Faça um programa que peça 4 notas bimestrais e mostre a média, usando listas.
'''

notas = []
for i in range(4):
    notas.append(float(input(f"Digite a {i + 1}º nota :\n")))
media = sum(notas) / len(notas)

print(f"Média final: {media}")
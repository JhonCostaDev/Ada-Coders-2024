lista1 = [1, 2, 3, 4, 5]

# Lista 2
lista2 = [6, 7, 8, 9, 10]

lista3 = []

for i in range(len(lista1)):
    lista3.append(lista1[i] + lista2[i])
    
for item in lista3:
    print(item)
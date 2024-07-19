''' 10 - Peque a lista gerada no exercício anterior e transforme cada um dos itens dessa lista em um float.
'''

lista_str = ['1', '43', '95', '03', '57']

lista_float = []

for item in lista_str:
    lista_float.append(float(item))
    
print(lista_float)
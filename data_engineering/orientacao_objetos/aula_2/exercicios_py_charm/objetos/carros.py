from modulos.Carro import Carro
#Instânciando um carro Celta
celta = Carro('Chevrolet', 'Celta', 1998, 'preto')
# Atribuindo um número de documento
celta.doc = 'h23442-3432J'
print(celta)

#Instânciando um carro Uno
uno = Carro('Fiat', 'Uno-Miller', 2008, 'Azul', num_portas=4)
# Atribuindo uma placa
uno.placa = 'HYB-4382'
print(uno)

#Instânciando um carro Gol
gol = Carro('VolksWagen', 'Gol', 2000, 'Prata', num_portas=4)
gol.placa = 'HUY-9043'
gol.doc = 'YB2873023987489U'
print(gol)


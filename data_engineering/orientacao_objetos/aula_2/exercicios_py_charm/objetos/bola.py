from modulos.esfera import Esfera
# Instância do objeto bola
bola = Esfera(5)
# Método para calcular a área
area = bola.area()
#print(f'{area:.2f}')
# Método para calcular o volume de superfície
vol = bola.volume()
#print(f'{vol:.2f}')

#Exibindo os resultados com o método mágico __repr__
print(bola)
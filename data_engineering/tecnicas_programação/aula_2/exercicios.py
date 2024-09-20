
'''
1 - Utilize comprehension para gerar a lista de todos os números interios entre 0 e 19. Converta a lista em um numpy array bidimensional (matriz) com 4 linhas e 5 colunas.
'''
#%%
import numpy as np
lista = [num for num in range(20)]
print("==== Lista ====:\n", lista)

array = np.array(lista)
print("\n==== Array ====:\n", array)

matriz = array.reshape((4,5))
print("\n==== Matriz ====:\n", matriz)

# %%
'''
2 - Construa um array unidimensional com 30 números inteiros escolhidos de forma randômica no intervalo entre 0 e 20. Reformate o array para que se torne uma matriz A com 5 linhas e 6 colunas
'''
array = np.linspace(0, 20, 30)
array

matriz = array.reshape((5, 6))
matriz
# %%
import numpy as np
array = np.arange(1, 201).reshape((20, 10))
# linhas
array[[1, 5, 8],:]
# colunas
array[:,[1, 5, 8]]

# %%
array[::2]
# %%

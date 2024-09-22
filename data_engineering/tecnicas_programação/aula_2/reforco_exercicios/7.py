# ### Exercício 7)
# Construa uma função chamada `ordena_linhas` que recebe uma matriz como parâmetro e troque as linhas de posição para que fiquem ordenadas de acordo com a primeira coluna. Por exemplo:
# ```python
# A = np.array([[20, 26, 12], 
#               [8, 3, 26], 
#               [3, 10, 4]])
# print(ordena_linhas(A))
# ```
# deve resultar em
# ```python
# [[ 3 10  4]
#  [ 8  3 26]
#  [20 26 12]]
# ```
#%%
import numpy as np
lista = [[20, 26, 12], 
              [8, 3, 26], 
               [3, 10, 4]]
lista
# %%
array = np.array(lista).reshape((3,3))
array
# %%
def ordenar_linhas(array):
    ordenado = array[array[:, 0].argsort()]
    return ordenado
# %%
array_ordenado = ordenar_linhas(array)
array_ordenado
# %%
array
# %%

#%%
import numpy as np
# %%
matriz = np.arange(1, 10).reshape((3,3))

matriz
# %%
# Metodos
# Achatar matriz
matriz.flatten()
# %%
# Achatar matriz
matriz.ravel()
# %%
# ou também, argumento é a quantidade de elementos do array seguido da vírgula, pois queremos apenas uma dimensão.
matriz.reshape(9,)
# %%
# Entendendo a diferança entre flatten e ravel

matriz

# %%
m_flatten = matriz.flatten()
m_flatten[2] = 100
m_flatten
# %%
matriz
# %%
m_ravel = matriz.ravel()
m_ravel[-1] = 100
m_ravel
# %%
matriz
# %%
# Usando o flatten, quando eu atribui um array/matriz a uma variável usando flatten, se eu modificar essa nova matriz, minha matriz original não será alterada. 

# Usando ravel: se eu criar uma nova matriz/array usando uma matriz original.ravel() e depois eu alterar algum elemento dessa nova matriz. a matriz original também terá o seu elemento alterado 



# %%
# Trânsposta: O que é coluna vira linha e o que é linha vira coluna
matriz.T

# Produto interno. Numpay DOT

matriz1 = np.ones(3)
matriz2 = np.array([3,3,3])
produto_interno = np.dot(matriz1, matriz2)
produto_interno
# %%

## RANDOM CHOISE, sorteia um número de uma lista
import random
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

random.choice(lista)
# %%
# RANDOM CHOISE DO NUMPY
# RETORNA UM ARRAY COM A QUANTIDADE DE ELEMENTOS QUE QUISERMOS
np.random.choice(lista, 3)
# %%

# ARGSORT
vetor = np.array([12, 5, 38, 20, 21, 3, 23, 75, 2, 74])
mascara = vetor.argsort()

ordenado = vetor[mascara]
# %%
ordenado
# %%
# ASTYPE - CONVERTE TODO O ARRAY EM UM TIPO

ordenado.astype(str) 


# %%


# MASCARA BOOLEANA
# array[comparação booleana]
ordenado.astype(float)
# %%
ordenado[ordenado >30]
# %%
mascara = ~ (ordenado < 10)
ordenado[mascara]
# %%


# NUMPAY WHERE
# Parece mto operação ternária

ate_100 = np.arange(100)
# %%
ate_100_pares = np.where(ate_100 % 2 == 0, ate_100, -1)
# %%
ate_100_pares[ate_100_pares != -1]
# %%

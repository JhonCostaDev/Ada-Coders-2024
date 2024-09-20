# ### Exercício 4)
# Construa um array `A` bidimensional 5x6 com 30 números inteiros escolhidos de forma randômica no intervalo entre 0 e 20. 
# - faça uma cópia do array `A` criado, chamando a cópia de `Ac`
# - Substitua todos os elementos do array `A` que sejam maiores que 10 pelo valor -1 
# - Substitua todos os elementos do array `Ac` que sejam maiores que 7 e menores que 15 pelo valor -1 

# __Dica:__ Gere máscaras booleanas para realizar as modificações nos arrays.
#%%
import numpy as np 

matriz = np.random.randint(0, 20, size=30).reshape((5,6))
matriz

matriz_a = matriz.copy()
# %%
matriz[matriz > 10] = -1
matriz
# %%

matriz_a[(matriz_a > 7) & (matriz_a < 15)] = -1
matriz_a

# %%

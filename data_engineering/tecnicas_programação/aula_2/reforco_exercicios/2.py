# ### Exercício 2)
# Construa um array unidimensional com 30 números inteiros escolhidos de forma randômica no intervalo entre 0 e 20. Reformate o array para que se torne uma matriz `A` com 5 linhas e 6 colunas.
#%%
import numpy as np 
matriz = np.random.randint(0, 20, size=30).reshape((5,6))

matriz
# %%
# usando o choice

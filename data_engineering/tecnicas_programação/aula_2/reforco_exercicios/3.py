# ### Exercício 3)
# Crie uma __view__ da matriz `A` gerada na célula anterior contendo:
# - as linhas de `A` com índices 0,1 e 3
# - as linhas de `A` com índice 1 e 2 e as colunas com índice 0,2 e 4
# - as linhas de `A` com índice 1 e 3 e as colunas com índice 1 e 3
#%%
import numpy as np 

matriz = np.random.randint(0, 20, size=30).reshape((5,6))
# %%
print(matriz)
view_1 = matriz[[0,1,3],:]
view_1
# %%
view_2 = matriz[[1, 2],:][:,[0, 2, 4]]
view_2
# %%

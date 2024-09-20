# ### Exercício 5)
# Construa um array `A` com 20 linhas e 10 colunas onde os elementos são os números interios de  1 até 200.
# - Crie uma __view__ de `A` chamada `A_lpares` contendo apenas as linhas de `A` com índice par.
 
# - Crie uma __view__ de `A` chamada `A_lpares_cimpares` contendo as linhas `A` com índice par e colunas com índice ímpar.
#%% 
import numpy as np
matriz = np.arange(1,201)

view_a = matriz[::2] 
# %%
view_a = matriz[::2]
view_a
# %%
view_b = matriz[::2, 1::2]
view_b
# %%
 #a[::2, 1::2]
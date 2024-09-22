# ### Exercício 6)
# Substitua os elememtos do array `A` do exercício anterior por -1 quando pelo menos um dos índices do elemento é par. 

# __Dica:__ Construa uma máscara booleana
#%%
import numpy as np 
a = np.arange(1, 201).reshape((20, 10))

a
# %%
#a[::2 , ::2] 
a[::2] = -1
a[:, ::2] = -1

a
# %%

#TODO: entender melhor essa sintaxe
b = np.arange(1, 201).reshape((20, 10))

b[(np.arange(20)[:, None] % 2== 0) | (np.arange(10) % 2 == 0)] = -1
b


# %%

# %%
c = np.arange(1, 201).reshape((20, 10))
c
# %%
mascara = (np.arange(20)[:, None] % 2== 0) | (np.arange(10) % 2 == 0)

# %%
c[mascara] = -1
# %%
c
# %%

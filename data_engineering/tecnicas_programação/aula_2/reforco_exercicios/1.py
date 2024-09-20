### Exercício 1)
# Utilize comprehension para gerar a lista de todos os números interios entre 0 e 19. Converta a lista em um numpy array bidimensional (matriz) com 4 linhas e 5 colunas.
#%%

#list comprehension
numeros = [num for num in range(20)]
numeros
# %%
import numpy as np
# Convertendo
matriz = np.array(numeros).reshape((4,5))
matriz


# %%

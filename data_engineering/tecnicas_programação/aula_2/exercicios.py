
'''
1 - Utilize comprehension para gerar a lista de todos os números interios entre 0 e 19. Converta a lista em um numpy array bidimensional (matriz) com 4 linhas e 5 colunas.
'''
#%%
import numpy as np
lista = [num for num in range(20)]
print(lista)

matriz = np.array(lista)
matriz

# %%

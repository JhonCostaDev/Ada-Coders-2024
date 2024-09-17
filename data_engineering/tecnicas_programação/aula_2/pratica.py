#%%
import numpy as np

# Converter uma lista em um array com numpy
numbers_1 = (42, 17, 89, 23, 56, 78, 34, 91, 65, 12)
array_numbers_1 = np.array(numbers_1)

print(array_numbers_1)


# Isso é uma lista de listas
#%%
sorteio = [
    [23, 45, 67, 89, 12, 34, 56, 78, 90, 21],
    [11, 22, 33, 44, 55, 66, 77, 88, 99, 10],
    [19, 28, 37, 46, 55, 64, 73, 82, 91, 20],
    [13, 26, 39, 52, 65, 78, 81, 94, 17, 30],
    [14, 25, 36, 47, 58, 69, 70, 81, 92, 13]
]
#%%
# transformando em array com numpy
array_sorteio = np.array(sorteio)
print(array_sorteio)


# ===================== ndim =====================
# retorna o número de dimensões
dimensoes = array_sorteio.ndim
dimensoes

# %%
# ===================== SHAPE =====================
# retorna uma tupla onde o primeiro elemento é o número de linhas e o segundo o número de colunas
a = array_sorteio.shape
a 

# %%
array_3d = np.zeros((2, 3, 4))
print(array_sorteio)  # Saída: 3

# ==============listas aninhadas ===================
# %%

lista_aninhada = [[1, 2, 3], [4, 5, 6]]

array_2d = np.array(lista_aninhada)

print(array_2d.shape)

# %%

# ===================== Arange =====================
# assim como no built-in do python onde temos o range que nos auxilia na geração de números, na biblioteca numpy temos o método arange

# ------------- built-in range -------------
a = list(range(0, 15, 5))

a 
# %%
# ------------- Numpy arange -----------------------
import numpy as np 

a = np.arange(0, 100, 1.8)
a


# %%
import numpy as np
# ================== LINSPACE =====================
# Vou utilizar o np.linspace quando eu quiser um array onde a diferença de um número para o outro seja igualment e espeçada.

# np.linspace(start, stop, esp)

array = np.linspace(10, 100, 2)
array



# %%
# Excluindo endpoint
array = np.linspace(1, 5, 10, endpoint=False)
array
# %%

# retornando passo
array, passo = np.linspace(0, 5, num=10, retstep=True)

print(f"Array: {array}\nPasso: {passo}")
# %%



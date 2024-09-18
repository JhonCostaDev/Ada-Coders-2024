#%%
import numpy as np

# Converter uma lista em um array com numpy
numbers_1 = (42, 17, 89, 23, 56, 78, 34, 91, 65, 12)
array_numbers_1 = np.array(numbers_1)

print(array_numbers_1)
type(array_numbers_1)
array_numbers_1

# Isso é uma lista de listas
#%%

sorteio = [
    [23, 45, 67, 89, 12, 34, 56, 78, 90, 21],
    [11, 22, 33, 44, 55, 66, 77, 88, 99, 10],
    [19, 28, 37, 46, 55, 64, 73, 82, 91, 20],
    [13, 26, 39, 52, 65, 78, 81, 94, 17, 30],
    [14, 25, 36, 47, 58, 69, 70, 81, 92, 13]
]

# transformando em array com numpy
array_sorteio = np.array(sorteio)
print(array_sorteio)


# ===================== ndim =====================
# retorna o número de dimensões
dimensoes = array_sorteio.ndim
print("===================== NDIM =====================")
print(f"NDIM: O array sorteio tem {dimensoes} dimensões")


# %%
# ===================== SHAPE =====================
# retorna uma tupla onde o primeiro elemento é o número de linhas e o segundo o número de colunas
linhas_sorteio, colunas_sorteio = array_sorteio.shape

print("===================== SHAPE =====================")
print(f"O array sorteio tem {linhas_sorteio} linhas e {colunas_sorteio} colunas") 

# %%

#===================== ZEROS =====================
# Constroi um array de números zeros
array_3d = np.zeros((2, 3, 4))
zero_dimensoes = array_3d.ndim
zero_blocos ,zero_linhas, zero_colunas = array_3d.shape

print(f"O array Zeros tem {dimensoes} dimensões, sendo {zero_blocos} blocos onde cada um tem  , {zero_linhas} linhas e {zero_colunas} colunas")
array_3d

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
# ================== ARANGE =====================
import numpy as np 

a = np.arange(0, 100, 1.8)
a


# %%
import numpy as np
# ================== LINSPACE =====================
# Vou utilizar o np.linspace quando eu quiser um array onde a diferença de um número para o outro seja igualment e espeçada.

# np.linspace(start, stop, esp)

array = np.linspace(1, 2, 5)
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

# =========== OPERAÇÕES ENTRE ARRAYS COM NUMPY =============
# Diferente das listas, operações matemáticas em arrays são realizadas, elemento por elemento. Os arrays devem ter o mesmo shape

janeiro = np.array([29.8, 32.1, 26.5])
fevereiro = np.array([23.2, 22.5, 51.2])

soma = janeiro + fevereiro
subtracao = janeiro - fevereiro
multiplicacao = janeiro * fevereiro
divisao = janeiro / fevereiro

print(f"Soma: {soma}\nSubtração: {subtracao}\nMultiplicação: {multiplicacao}\nDivisão: {divisao}")
# %%

# =========== GERANDO NÚMEROS COM NUMPY =============
# Assim como na build-in do python, o numpy também consegue gerar números aleatórios

# Normal
num1 = np.random.normal()
print(num1)
# randint: precisa passar o intervalo desejado
num2 = np.random.randint(0,10)
print(num2)



# %%
# ==================== MATRIZES ============================

# Na matemática, matrizes são tabelas organizadas em linhas e colun, onde cada elemento é identificado por dois índice: Um para linha e outro para coluna.

# Uma matriz pode ser representada no formato (m X n) onde m é o número de linhas e n o número de colunas.
# Por exemplo, uma matriz (3 x 4) tem 3 linhas e 4 colunas.

# CRIANDO UMA MATRIZ 3X3 A PARTIR DE UMA LISTA

lista = [[2,5,8], [9, 4, 6], [7,3,1]]

matriz = np.array(lista)
matriz
# %%
# APLICANDO MÉTODOS NA MATRIZ

dimensoes = matriz.ndim
formato = matriz.shape
dimensoes
formato
# %%
lista = [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],[[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]]
matriz_3d = np.array(lista)
print(matriz_3d)
dimensoes = matriz_3d.ndim
formato = matriz_3d.shape
print(f"dimensões: {dimensoes}\nFormato: {formato}")
# %%
# outro exemplo

lista = [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],[[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]],[[25, 26, 27, 28], [29, 30, 31, 32], [33, 34, 35, 36]]]

matriz_3d = np.array(lista)
print(matriz_3d)
dimensoes = matriz_3d.ndim
formato = matriz_3d.shape
print(f"dimensões: {dimensoes}\nFormato: {formato}")

# %%

# CRIANDO MATRIZES PASSANDO FORMATOS COMO PARÂMETRO

matriz_zero = np.zeros((3, 3))# tem que passar dentro de uma tuplas
matriz_zero
# %%
matriz_ones = np.ones((2, 5))
matriz_ones

# %%
matriz_3d
eixos = matriz_3d.ndim
blocos, linhas, colunas = matriz_3d.shape
elementos = matriz_3d.size
bites = matriz_3d.itemsize

print(f"""
Essa matriz tem:
{eixos} eixos
{blocos} blocos
{linhas} linhas
{colunas} colunas
{elementos} elementos
cada elemento ocupa {bites} bites em memoria.
""")
# %%


# ============ EXEMPLO DO PROFESSOR

array = np.linspace(0, 2, 30)

print(array)
print("Atributos desse array")

eixos = array.ndim
linha = array.shape
elementos = array.size
bites = array.itemsize
tipo = array.dtype
dados = array.data

print(f"""
Essa matriz tem:
{eixos} eixos

{linha} linha
{elementos} elementos
cada elemento ocupa {bites} bites em memoria.
{tipo} tipo
{dados} endereço de memória
""")
# %%

# Criar uma matriz identidade de 8 dimensões

identidade = np.identity(8)
print(identidade)

print(f"""
{identidade.ndim} dimensoes
{identidade.shape} formato
{identidade.size} numero de elementos
{identidade.dtype} tipo de dados
{identidade.itemsize} tamanho em bits
{identidade.data} local em memoria
""")
# %%

# OPERAÇÕES MATEMÉTICAS
# É realizado operações em cada elemento do array.

array = np.arange(4, 20, 2)
print(f"Array original\n{array}\n")
print(f"Somando mais 2: \n{array + 2}\n")
print(f"Subtraindo 2: \n{array - 2}\n")
print(f"Multiplicando com  2: \n{array * 2}\n")
print(f"Dividindo por 2: \n{array / 2}\n")
print(f"Divisão inteira por 2: \n{array // 2}\n")
print(f"Elevando ao quadrado: \n{array ** 2}\n")
print(f"Resto da divisão por 2: \n{array % 2}\n")
print(f"Inverso: \n{1 / array}\n")


# %%
# RELEMBRANDO
#List Comprehension


quadrados = []
for num in range(11):
    if num % 2 == 0:
        quadrados.append(num * num)
        
quadrados
# %%
#######################################

quadrados_comprehension = [num * num for num in range(11) if num % 2 == 0]
print(quadrados_comprehension)
# %%

# Ainda sobre numpy
import numpy as np 

# arange: semelhante ao range, gera em sequencia e permite numeros de ponto flutuante como passo
arr = np.arange(12)
print(arr)

#Linspace: passo um ponto inicial, um final e a quantidade de números que quero, ele me dá a quantidade espaçada igualmete. 
arr2 = np.linspace(1, 10, 12)
print(arr2)

# Ones: me gera um array/matriz de números (1).
arr3 = np.ones(12)
#np.zeros(2) - semelhante

# Operações matemáticas em arrays são computadas elementos por elementos, por isso os arrays precisam ter o mesmo shape(formato/tamanho) para não dar erro.
resultado = arr + arr2 + arr3
print(resultado)
print(resultado.shape)
print(resultado.size)

# Diferença entre (shape e size)

vetor = np.random.randint(1, 25, size=50).reshape((10,5))
print(vetor)
print(f'Len: {len(vetor)}') # número de linhas
print(f'Shape: {vetor.shape}') # linhas x colunas
print(f'Size: {vetor.size}') # número de elementos

# achata a matriz, uma dimensão
vetor_flatten = vetor.flatten()
print(vetor_flatten)

vetor_ravel = vetor.ravel()
print(vetor_ravel)

# Também podemos fazer isso com Reshape

vetor_reshape = vetor.reshape((vetor.size,))
print(vetor_reshape)


# Matriz Transposta: Inverte linhas e colunas
# .Tezão
print(vetor.T)

# Método de produto interno / produto escalar

a = np.random.randint(1, 10, size=5)
b = np.random.randint(1, 10, size=5)

produto_interno = np.dot(a, b)
print(produto_interno)


# Numpy resolve problemas de algebra linear

# random choice
lista = [1,2,3,4,5,6]
nume = np.random.choice(lista) # sorteando um da lista
print(nume)

# Adimite parâmetro, no size especifica quantos elementos eu quero retornar

nume2 = np.random.choice(lista, 2)
print(nume2)

# e ainda posso passar que não quero números repetidos

nume3 = np.random.choice(lista, 3, replace=False)
print(nume3) 

# Argsort: Retorna um array com os índices dos elementos na ordem dos valores

arg_sort = np.random.randint(1, 50, size=15)
print(arg_sort)
print(arg_sort.argsort())

# Astlype: Trocar o tipo da variável

array_string = arg_sort.astype(str)
print(arg_sort)
print(array_string)


# Máscara Booleana

ar50 = np.random.randint(1, 20, 20)
# Isso é uma máscara booleana
mascara = ar50>10
print(ar50[mascara])

# Verificando a existência de elemento repetidos

# uso a função unique que retorna os elementos únicos do array e a contagem de cada elemento
unicos, counts = np.unique(ar50, return_counts=True)
print(unicos) # array sem repetição
print(counts) #
numero_repetidos = counts > 1
print(numero_repetidos)
elementos_repetidos = unicos[numero_repetidos]

print(ar50)
print(elementos_repetidos)


# Máscara booleana composta

mb = (ar50 > 5 )& (ar50 < 10)
print(ar50[mb])

# Substituindo valores com máscara booleana

# Crio um array com 100 elementos
ate100 = np.arange(100)
print(ate100)

# Usando where, ele vai substituir todo elemento cuja a condição não seja atendida por 0, no caso contratio ele mantem o elemento
resultado = np.where(ate100 % 2 != 0, 0, ate100)
print(resultado)

# uso a máscara booleana para tirar os elementos (0), deixando só os elementos desejados.
resultado = resultado[resultado != 0]
print(resultado)

# ================ PANDAS ================


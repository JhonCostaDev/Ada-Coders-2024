# ================ PANDAS ================
import numpy as np
import pandas as pd 

array = np.random.randint(1, 50, size=10)

print(array)

# Posso converter lista ou array
# Indexa elementos numa estrutura de series.
serie = pd.Series(array)
print(serie)


# Aceita outras tipagens de dados, respeitando sempre tipágem única

frutas = ['banana', 'uva', 'morango', 'goiaba']

print(pd.Series(frutas))

# Com Dicionários

preco_frutas = {
    "banana": 2.75,
    "uva": 7.90,
    "morango": 12.75,
    "goiaba": 6.99
}

serie_preco_frutas = pd.Series(preco_frutas)
print(serie_preco_frutas)

# Posso pegar os values do dicionário na forma de um array
precos = serie_preco_frutas.values
print(precos)

#=======================================================

dicionario = {"lapis": 1.5, "borracha": 0.50, "caneta": 3.45 }

serie_dicio = pd.Series(dicionario)
print(serie_dicio)

# Indexação
print(dicionario.keys())
print(serie_dicio.keys())
print(dicionario.values())
print(serie_dicio.values)


# Consigo isolar os elementos pelo índice
# com series utilizo indices positivos

print(serie)
print(serie[0])

## usando slice
# Pegando fatias da minha serie

serie_slice = serie[3: 6]
print(serie_slice)

# Labels: Podemos atribuir indices personalizados para cada elemento e acessá-los por esses índices. 

lista = [43, 46, 72, 87, 90, 43 , 2 ,27,  5, 18]

print(len(lista)) 

# Defino um alista de indices
indices = ['a', 'b', 'c', 'd', 'e' ,'f', 'g', 'h', 'i', 'j']
print(len(indices))
print(indices)

lista_indexada = pd.Series(index=indices, data=lista)
print(lista_indexada)

# Operações Matemáticas

# Posso fazer operações matemáticas com a minha série. Semelhante ao array, a operação será executada a cada elemento 
print(serie_preco_frutas)

# somar 1 ao valor de cada fruta do meu dicionario/serie de frutas

serie_preco_frutas += 1
print(serie_preco_frutas)
# Multiplicando
serie_preco_frutas *= 2
print(serie_preco_frutas)


# ============= Métodos Pandas ============= 


notas = [8.23, 3.45, 7.89, 2.34, 9.01, 5.67, 4.56, 6.78, 1.23, 0.45, 8.67, 3.21, 7.65, 2.98, 9.34, 5.12, 4.89, 6.45, 1.78, 0.98, 8.12, 3.56, 7.34, 2.67, 9.78, 5.34, 4.12, 6.89, 1.45, 0.67, 8.45, 3.78, 7.12, 2.45, 9.56]

seria_notas = pd.Series(notas)
print(seria_notas)

# SORT_VALUES: Ordena os valores mantendo os índices originais

print(seria_notas.sort_values())

# UNIQUE:  Retorna valores distintos da serie

unicos = seria_notas.unique() 
print(pd.Series(unicos))

notas2 = [ 6.9, 5.4, 10.0, 5.4, 8.3, 6.9]
s_notas2 = pd.Series(notas2)
print(s_notas2.unique())

# Nunique: Retorna a quantidade de valores distintos
print(s_notas2.nunique())

# Value_counts: Retorna as frequencias(contagens) para cada um dos elementos distintos dentro de uma seria.

print(s_notas2.value_counts())
print(seria_notas.value_counts())

# Posso passar parâmetro e receber como resultado a porcentagem de ocorrencias daquele valor

print(seria_notas.value_counts(normalize=True))

print(s_notas2.value_counts(normalize=True))

# Posso também passar o parâmetro bins que me retornará um histograma

print(s_notas2.value_counts(normalize=True, bins=5)* 100)

# rack

resultado = s_notas2.value_counts(normalize=True, bins=5).mul(100).round(2).astype(str) + "%"

print(resultado)

notas = pd.Series([9., 8., 10., 6.5, 4.5, 5., 7.5, 8.5, 4., 6., 1., 0., 7. ])

unicas = notas.unique()
nunicas = notas.nunique()
conta_valores = notas.value_counts()
normalizadas = notas.value_counts(normalize=True)
bins = notas.value_counts(normalize=True, bins=5)
formatada = notas.value_counts(normalize=True, bins=5).mul(100).round(2).astype(str) + "%"

print(formatada) 

# Utilizando os métodos numpy
#TODO: Fazer amanhã

# Describe
descricao = notas.describe().round(2).astype(str) + ' uni'
print(descricao)





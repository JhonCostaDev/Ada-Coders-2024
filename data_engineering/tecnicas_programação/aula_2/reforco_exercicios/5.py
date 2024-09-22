# ### Exercício 5)
# Construa um array `A` com 20 linhas e 10 colunas onde os elementos são os números interios de  1 até 200.
# - Crie uma __view__ de `A` chamada `A_lpares` contendo apenas as linhas de `A` com índice par.
 
# - Crie uma __view__ de `A` chamada `A_lpares_cimpares` contendo as linhas `A` com índice par e colunas com índice ímpar.
#%% 
# Import da biblioteca numpy
import numpy as np 

# %%
# Criei um avariável chamada a, e atribuí a ela um numpy. arange, que gerará o array com os números de 1 a 200 e em seguida utilizei a função reshape para dar a forma pedida 20 linhas por 10 colunas
a = np.arange(1, 201).reshape((20, 10))

# utilizei o atrubuto shape só para verificar se o formato estava correto
a.shape
# %%
# com a matriz na forma correta, agora é só fazer um slice, onde eu chamo o meu array indexando com starte e stop em branco, porém com passo 2, assim só os indices pares serão exibidos
a_lpares = a[::2]
#a_lpares.shape
#a_lpares.size
#a_lpares.mean()

# %%
# A_lpares_cimpares
# linhas pares e colunas ímpares

# para visualizar as linhas de uma matriz no numpy usando slice, indexamos a variável, dentro dos colchetes separados por vírgula onde antes da vígula listamos as linhas e depois da vírgula listamos as colunas.
# %%
a_lpares_cimpares = a[::2, 1::2]
a_lpares_cimpares
# %%

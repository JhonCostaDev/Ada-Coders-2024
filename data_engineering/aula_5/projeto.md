link do colab
https://colab.research.google.com/drive/1MQ7SFNtBWtDtLUvlSmuvn9LSlhiAb7vt?usp=sharing

K-Nearest Neighbors - KNN
Modelo supervisionado de machine learning que pode ser utilizado tanto para classificação, isto é, rotular os dados; quanto para regressão, ou seja, aproximar valores.

Características
Simples
Interpretável
Largamente conhecido e estudado
Razoavelmente rápido
Por conta disso é um ótimo benchmark

Algoritmo
Passo 1: Definir um valor para K
Passo 2: Definir os K vizinhos mais próximos do ponto a ser classificado de acordo com uma função de distância.
Passo 3:
Se for um problema de Regressão: Calcular a média de todos os vizinhos.
Se for um problema de Classificação: Calcular a moda de todos os vizinhos.
Passo 4: Atribuir o valor/classe ao ponto de interesse conforme cálculo do Passo 3.
Links Úteis
Definições
"Primeira" aparição do modelo
Expansão do KNN
Casos de uso
Click Stream
Battery life
Mahalanobis Distance
Dataviz
Stanford
IRA
Definição do Problema
Dados
Os dados abaixo são referentes ao cadastro de clientes de uma empresa de investimentos com suas respectivas carteira de investimentos, que indica se esse cliente tem o perfil de investidor Conservador, Moderado ou Agressivo. O nosso intuito é, a partir do investimento de alguns clientes que já tem um perfil definido, estimar esse perfil para aqueles que ainda não estão classificado, afim de oferecer novos produtos que sejam mais adequados a eles.

Os dados abaixo seguem o seguinte padrão:

[CPF: INT, Perfil Do Investidor: STRING, Carteira de Investimento: TUPLA]

Regras
Se você precisar de uma função para computar algo crie ela
Não é permitido usar nenhum módulo externo como numpy e math
Use apenas os objetos e fluxos visto até o momento no curso
Se você tiver dificuldade de trabalhar com mais de 2 dimensões, pode utilizar apenas os dois primeiros valores de cada tupla
O objetivo principal desse projeto não é encontrar o modelo de knn mais otimizado, mas sim você conseguir criar um modelo de KNN, independente se ele é o melhor ou não
Não precisa se preocupar com a normalização das dimensões. É algo que vocês não viram
Caso queira medir a distância utilizando a distância euclidiana
Como medir a distância euclidiana:

Euclidean_distance_2d.svg



Fórmula da distância euclidiana:

euclidean_distance_formula_multidimensional.svg

exemplo 1 de como calcular: https://www.omnicalculator.com/math/euclidean-distance

exemplo 2:

carteira1 : (x: 1, y: 1, z: 1)
carteira2 : (x: 2, y: 2, z: 1)
distância, é a raiz quadrada de: (2-1)2 + (2-1)2 + (1-1)2 em outras palavras: raiz quadrada de (1 + 1 + 0).

a distância entre esses dois pontos é de: 1.41

Se quiser dividir sua variavel data em base de treino e teste:
dos 120 eventos na variavel data: posso dividir entre uma base de treino e uma de teste.

treino: eu consigo definir qual a distância para classificar como conservador/moderado/agressivo

teste: eu consigo testar o aproveitamento baseado no treino.
treino1 =[
        ['cachorro', 'conservador',(1,1,1,1)], 
        ['gato', 'conservador',(1,1,2,1)],
        ['papagaio', 'moderado',(9,9,9,1)], 
        ['coelho', 'moderado', (9,9,8,1)] ,
        ['urso','agressivo',(4,5,9,1)],
        ['lobo', 'agressivo',(7,8,5,1)], 
]

teste1 = [['onitorrinco', '',(3, 7, 1,1)],
         ['jacare', '',(5, 2, 8,1)],
         ['leao', '',(9, 4, 6,1)],
         ['tigre', '',(1, 3, 7,1)],
         ['jumento', '',(8, 5, 2,1)],
         ['cavalo', '',(4, 9, 3,1)],
         ] #teste = [1.2,1.3,2]

def ordenar(lista):
    return lista[-1]

def calcular_raiz(n):
    return n ** 0.5



def calcular_distancia(base_dados, novo_dado):
    
    distancia_euclidiana = {}
    distancia_resultados = []
    distancia_ordenada = []
    k_proximos = []
    
    for carteira in base_dados:
        distancia = 0
        cliente_base = carteira[0]
        classificacao = carteira[1]
        carteira_base = carteira[2]
        nova_carteira = novo_dado[2]
        novo_cliente = novo_dado[0]
        
        for i in range(len(nova_carteira)):
            distancia += (carteira_base[i] - nova_carteira[i]) ** 2

        delta_distancia = [cliente_base, classificacao, calcular_raiz(distancia)]
        distancia_resultados.append(delta_distancia)
        distancia_ordenada = sorted(distancia_resultados, key=ordenar)
        
        
        distancia_euclidiana[novo_cliente] = k_proximos
        
    for i in distancia_ordenada:
            
        k_proximos.append(i[1])
        
        
    return distancia_euclidiana

def calcular_moda(lista, k):
    menores = []
    for item in range(k):
        menores.append(lista[item])
    
    conservador = menores.count('conservador')
    moderado = menores.count('moderado')
    agressivo = menores.count('agressivo')
            
    if conservador > moderado and conservador > agressivo:
                #print(f'a chave {chave} classifica como conservador')
        return 'conservador'
    elif moderado > conservador and moderado > agressivo:
                #print(f'a chave {chave} classifica como moderado')
        return 'moderado'
    else:
                #print(f'a chave {chave} classifica como agressivo')
        return 'agressivo'
            #print(tres_proximos)
    return menores   
       
    
def classificar(base_dados, novos_dados):
    classificacao = ''
    k = 3
    for novo_dado in novos_dados:
        
        dicionario = calcular_distancia(base_dados, novo_dado)
        for chave, valor in dicionario.items():
            novo_dado[1] += calcular_moda(valor, k)
            #print(f'{chave} = {valor}')
            # tres_proximos = calcular_moda(valor, k)
            # conservador = tres_proximos.count('conservador')
            # moderado = tres_proximos.count('moderado')
            # agressivo = tres_proximos.count('agressivo')
            
            # if conservador > moderado and conservador > agressivo:
            #     #print(f'a chave {chave} classifica como conservador')
            #     novo_dado[1] += 'conservador'
            # elif moderado > conservador and moderado > agressivo:
            #     #print(f'a chave {chave} classifica como moderado')
            #     novo_dado[1] += 'moderado'
            # else:
            #     #print(f'a chave {chave} classifica como agressivo')
            #     novo_dado[1] += 'agressivo'
            # #print(tres_proximos)
        #print(novo_dado)
    return novos_dados
       
    

x = classificar(treino1, teste1)
for i in x:
    print(i)


    
    

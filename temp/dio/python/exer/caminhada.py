''' Se eu sair de casa as 6:52 e correr 1km a um certo passo (8min 15s / km), entao 3km a 
um passo mais rápido (7min 12s / km) e 1km ao mesmo passo usado no primeiro km. Que hora 
eu chego em casa? '''
# saiu 6:52
def min_to_seg(min, seg):
	return (min * 60) + seg

hora_saida = '06:52'




#print(min_to_seg(8,15))
primeiro_trecho = min_to_seg(8, 15)
segundo_trecho = min_to_seg(7, 12) * 3
#print(segundo_trecho)
terceiro_trecho = primeiro_trecho

duracao_caminhada = primeiro_trecho + segundo_trecho + terceiro_trecho
print(f"{duracao_caminhada} segundos")


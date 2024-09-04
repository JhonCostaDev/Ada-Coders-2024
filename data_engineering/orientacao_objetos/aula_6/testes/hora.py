#%%
# Criar um programa para somar Horas.

# Suponha que eu receba uma string como dados de horas como no formato abaixo.
tempo = '15:27:54'

# Primeiro vou converter essa string para inteiro e então atribuir cada número a uma variável

#print(tempo.split(':'))   
# okay, conseguimos dividir, agora vamor atriuir cada um dos valores a uma respectiva variável
# %%

# Usando a forma mais tradicional
# h, m, s = tempo.split(':')
# h = int(h)
# m = int(m)
# s = int(s)


# Usando uma forma mais bonita

# h, m, s = map(int, tempo.split(":"))
# print(f'Hora: {h}, Minuto: {m}, Segundo: {s}')

# Acima utilizei o map para iterar sobre a lista que será criada pelo método split, passando a função int() para converter as strings em números inteiros

# Agora eu posso criar uma função que converte a minha string horas em segundo

def horas_para_segundos(hora:str) -> int:
    horas, minutos, segundos = map(int, hora.split(":"))
    return horas * 3600 + minutos * 60 + segundos

def segundos_para_horas(segundos_a_converter:int) -> str:
    horas = segundos_a_converter // 3600
    minutos = (segundos_a_converter % 3600) // 60
    segundos = segundos_a_converter % 60
    return f"{horas}:{minutos}:{segundos}"
    


# Na mão temos agora duas funções, uma que converte uma string em formato de horas para segundos, e outra que converte esses segundos para o formato de horas novamente.

# Agora podemos criar uma terceira função que será utilizada para somar o "tempo"

def soma_horas(hora_1, hora_2):
    segundos_1 = horas_para_segundos(hora_1)
    segundos_2 = horas_para_segundos(hora_2)
    
    soma_segundos = segundos_1 + segundos_2
    return segundos_para_horas(soma_segundos)

# testando
# eu saí de casa exatamente as 15:27:54, caminhei por 48 minutos e 19 segundos, que horas eu voltei para casa
#
saida = '15:27:54'
tempo = '00:48:19'

resultado = soma_horas(saida, tempo)
resultado

    
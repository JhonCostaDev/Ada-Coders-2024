'''def calcular_total(numero):
        return sum(numero)

def retorna_antecessor_e_sucessor(numero):
        antecessor = numero -1
        sucessor = numero + 1
        return antecessor, sucessor

print(calcular_total([10, 20, 34]))            # 64

print(retorna_antecessor_e_sucessor(10))
'''
'''
#```python
def salvar_carros(marca, modelo, ano, placa):
        print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carros("Fiat", "Palio", 1999, "ABC-6534")


salvar_carros("Chevrolet", "Celta", 2009, "YXC-9056")
'''

#```python
def exibir_poema(data_extenso, *args, **kwargs):
        texto = "\n".join(args)
        meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
        mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
        print(mensagem)

exibir_poema("Zen of Python", "Beautiful is better than ugly.", autor="Tim Peters", ano=1999)

#salvar_carros("VolksWagen", "Gol", 2004, "PKX-5417")

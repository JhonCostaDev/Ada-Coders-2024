# Funçoes em Python

Funçao é um bloco de código identificado por um nome e pode receber uma lista de parametros que
 podem ou nao ter valores padroes. Usar funçoes torno o código mais legível e posssibilita o 
reaproveitamento do código. Programar baseado em funçoes, é o mesmo que dizer que estamos 
programando de maneira estruturada.

```python
def show_message():
	print("Hello, world")

def show_message2(name):
	print(f"Welcome {name}!")

def show_message3(name="jhon"):
	print(f"Welcome {name}!")

show_message(): 			# $ Hello, world

show_message2(name = "jhon"): 		# $ Welcome jhon! 

show_message3(): 			# $ Welcome jhon
```
## Retornando valores

Para retornar um valor, utilizamos a palavra reservada **return**. 
Toda funçao retorna **None** por padrao. Diferente de outras linguagens de programaçao,
**em python uma funçao pode retornar mais de um valor**.

```python

def calular_total(numero):
	return sum(numero)

def retorna_antecessor_e_sucessor(numero)
	antecessor = numero -1
	sucessor = numero + 1
	return antecessor, sucessor

calcular_total([10, 20, 34]) 		# 64

retorna_antecessor_e_sucessor(10)	# (9, 11)

```

## ARGUMENTO NOMEADOS
Funçoes também podem ser chamadas usando argumentos nomeados da forma **chave=valor**

```python
def salvar_carros(marca, modelo, ano, placa):
	print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carros("Fiat", "Palio", 1999, "ABC-6534")

#argumentos posicionados
salvar_carros(marce="Chevrolet", modelo="Celta", ano=2009, placa="YXC-9056")

# Passando através de dicionário
salvar_carros(**{"marca": "VolksWagen", "modelo": "Gol", "ano": 2004, "plca": "PKX-5417")

```

## ARGS e KWARGS
Podemos combinar parametros obrigatórios com args e kwargs. Quando esses sao definidos
(* args e **kwargs), o método recebe os valores como tupla e dicionário respectivamente.


```python
def exibir_poema(data_extenso, *args, **kwargs):
	texto = "\n".join(args)
	meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
	mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
	print(mensagem)

exibir_poema("Monday - jun 17 2024","Zen of Python", "Beautiful is better than ugly.", autor="Tim Peters", ano=1999)

```
## PARAMETROS ESPECIAIS
Por padrao, argumentos podem ser passados para uma funçao python tanto por posiçao quanto
explicitamente pelo nome. Para uma melhor legibilidade e desempenho, faz sentido restringir a 
maneira pelo qual argumenos possam ser passados, assim um desenvolvedor precisa apenas olhar
para a definiçao da funçao para determinar se os itens sao passados **por posiçao, por posicao e
nome, ou por nome**.

```python
'''
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
	-------	     ---------	     --------
	  |		   |		|-Keyword only	
	  |		   |		
	  |		   -Positional or KeyWord 
	  --positional only	
'''

#POSITIONAL ONLY

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
	print(modelo, ano, placa, motor, combustivel)


criar_carro("Palio", 1999, "UNB-6712", marca="Fiat", motor="1.0", combustivel="Gasolina") #valido

criar_carro(modelo="Palio", ano=1999, placa="UNB-6712", marca="Fiat", motor="1.0", combustivel="Gasolina") #invalido

#KEYWORD ONLY - TODOS SAO PASSADOS POR POSIçAO
def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
	print(modelo, ano, placa, motor, combustivel)

criar_carro("Palio", 1999, "UNB-6712", "Fiat", "1.0", "Gasolina") #valido

criar_carro(modelo="Palio", ano=1999, placa="UNB-6712", marca="Fiat", motor="1.0", combustivel="Gasolina") #invalido

#KEYWORD AND POSITIONAL ONLY

def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
	print(modelo, ano, placa, motor, combustivel)


criar_carro("Palio", 1999, "UNB-6712", marca="Fiat", motor="1.0", combustivel="Gasolina") #valido

criar_carro(modelo="Palio", ano=1999, placa="UNB-6712", marca="Fiat", motor="1.0", combustivel="Gasolina") #invalido


```
## OBJETOS DE PRIMEIRA CLASSE
Em python tudo é objeto, dessa forma **funçoes também sao objetos**, o que as tornam objetosde
primeira classe. Com isso podemos **atribuir funçoes a variáveis, passá-las como parametro para
funçoes, usá-las como valores em estruturas de dados**(listas, tuplas, dicionários, etc) e usar
como valor de retorno pra uma funçao (closures). 
```python
def somar(a, b):
	return a + b

def exibir_resultado(a, b, funcao):
	resultado = funcao(a, b)
	print(f"O resultado da operaçao {a} + {b} = {resultado}")

exibir_resultado(10,54, somar)
#atribuir uma funçao a uma variável
op = somar

print(op(45, 23)) # 68

```

## ESCOPO LOCAL E ESCOPO GLOBAL
Python trabalha com escopo local e global, dentro do bloco da funçao o escopo é local.
Portatno, alteraçoes ali feitas em objetos imutáveis serao perdidas quando o método terminar de 
ser executado. Para usar objetos globais, utilizamos a palavra chave **global**, que informa
ao interpretador que a variável que está sendo manipulada no escopo local é global.
Essa **NAO é uma boa prática e deve ser evitada**.

```python
salario = 2000 #escopo global

def salario_bonus(bonus):
	global salario
	salario += bonus
	return salario

salario_bonus(500) 	#2500


``` 


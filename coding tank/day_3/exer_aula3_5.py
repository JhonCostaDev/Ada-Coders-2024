'''
5) Faça um script que peça para o usuário digitar a idade, o salário e o sexo de uma pessoa até que as entradas digitadas sejam válidas.

a. Idade: entre 0 e 150
b. Salário: maior que 0
c. Gênero: M, F ou Outro

'''
print("Entrada de dados")

idade = int(input("Digite sua idade\n"))
while idade < 0 or idade > 150:
    print("Idade inválida, digite um valor de 0 à 150")
    idade = int(input("Digite sua idade\n"))
    

salario = float(input("Digite seu salário: \n"))
while salario < 0:
    print("Salário Inválido, digite um valor acima de 0")
    salario = float(input("Digite seu salário: \n"))
print("Salário: ",salario)

genero = input("Digite seu Gênero: (M)masculino, (F)feminino (Outro)outros\n").upper()
while genero != 'M' and genero != 'F' and genero != "OUTRO":
    print("Gênero inválido - Digite M para masculino, F para feminino e outro para outras classificações de gênero.")
    genero = input("Digite seu Gênero: (M)masculino, (F)feminino (Outro)outros\n").upper()
print('''
    IDADE: {idade}
    SALÁRIO: R$ {salario}
    GÊNERO: {genero}
      ''')
    

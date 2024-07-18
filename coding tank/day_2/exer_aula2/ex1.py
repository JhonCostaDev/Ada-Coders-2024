# Exercício
'''nome = input("Digite seu nome:\n")
idade = int(input("Digite sua idade:\n"))
hobby = input("Qual é seu hobby?\n")
print("Meu nome é" + nome)
print(f"Meu nome é {nome}, e tenho {idade} anos e gosto de {hobby}")
'''

# Solicite ao usuário que insira seu ano de nascimento. desconsiderando o mês do ano de nascimento, emita a mensagem dizendo  quantos anos

ano_nascimento = int(input("Digite o ano do seu nascimento:\n"))
ano_atual = 2024
idade = ano_atual - ano_nascimento
print(f"Você tem {idade} anos")

'''
Bruno Issamo
21:49
TODO: FaZER COM ESTÁ DESCRITO...

Imagine que você está implementando um sistema para verificar se os alunos de uma turma estudantil passaram na disciplina ou não. Para isso solicite que o usuário insira as notas das 4 provas realizadas por um estudante e calcule a média. Após isso, emita uma resposta booleana (True ou False) se o estudante passou na disciplina pensando que a média mínima para aprovação é que seja pelo menos 5.


Crie um algoritmo que calcule o IMC (índice de massa corporal). O IMC é calculado com a formula PESO/(ALTURA ^ 2). Para isso, coloque as informações nas variáveis e ao final apresente o resultado como no exemplo: "O IMC é 18"

Escreva um algoritmo que calcule (x + y) * (x + y). Os valores de x e y devem ser inseridos pelo usuário
'''
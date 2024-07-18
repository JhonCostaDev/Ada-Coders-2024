# Imagine que você está implementando um sistema para verificar se os alunos de uma turma estudantil passaram na disciplina ou não. Para isso solicite que o usuário insira as notas das 4 provas realizadas por um estudante e calcule a média. Após isso, emita uma resposta booleana (True ou False) se o estudante passou na disciplina pensando que a média mínima para aprovação é que seja pelo menos 5.

print("========= Média =========")

nota_1 = float(input("Digite a primeira nota: \n"))
nota_2 = float(input("Digite a segunda nota: \n"))
nota_3 = float(input("Digite a terceira nota: \n"))
nota_4 = float(input("Digite a quarta nota: \n"))

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

print("Aprovado? ", media >= 5)


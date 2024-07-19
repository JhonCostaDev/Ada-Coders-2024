'''
6) Faça uma calculadora. O usuário deve inserir qual a operação matemática ele deseja realizar e logo em seguida os dois números. O programa deve finalizar apenas quando o usuário digitar a opção "sair" no momento de escolha da operação matemática.
'''
print("====== Calculadora Python ======\n")

while True:
    menu = input(f'''Escolha uma das opções entre parênteses abaixo:
            (+) - SOMAR
            (-) - SUBTRAIR
            (*) - MULTIPLICARg
            (/) - DIVIDIR
            (sair) - SAIR
                    ''').lower()

    if menu != '+' and menu != '-' and menu != '*' and menu != '/'and menu != 'sair':
         print("Opção inválida.")
    elif menu == 'sair':
            break
    else: 
        numero_1 = float(input("Digite o primeiro número:\n"))
        numero_2 = float(input("Digite o segundo número:\n"))
        
        if menu == '+':
            print(f"SOMA: {numero_1} + {numero_2} = {numero_1 + numero_2}")
        elif menu == '-':
            print(f"SUBTRAÇÃO: {numero_1} - {numero_2} = {numero_1 - numero_2}")
        elif menu == '*':
            print(f"MULTIPLICAÇÃO: {numero_1} x {numero_2} = {numero_1 * numero_2}")
        elif menu == '/':
            #TODO: tratar o número 0.
            print(f"DIVISÃO: {numero_1} / {numero_2} = {numero_1 / numero_2}")
        
        



# DECLARAÇÃO DAS VARIÁVEIS GLOBAIS
saldo_usuario = 0       # Saldo.
saques_diario = 3       # Limite de saques diário.
limite_por_saque = 500  # Limite de valor por saque.
extrato = ""            # Registro das movimentações do usuário.
contador_operacoes = 1  # Contador de operações, será utilizado no extrato.


# Menu de opcoes
def  menu_inicial():
	
	return input( """
#####################################
	    Bem vindo ao
	     Python Bank
####################################
    Escolha uma das opcao abaixo

        [1] - Sacar
        [2] - Depositar
        [3] - Extrato
        [0] - Finalizar

####################################

""")


def deposito(saldo, contado_operacoes, extrato):
	saldo_atual = saldo
	deposito = input('Digite o valor em (R$) reais do Depósito:\n')
	if deposito < 0:    # Verifica se o valor é válido
            print("Valor inválido")
            print("Tente Novamente!")
        else:                               # Realiza a operação de depósito
            
            extrato += f"{contador_operacoes} - Depósito no valor de R${deposito:.2f}\n" # Registra a operação no extrato.
            contador_operacoes += 1         # Registra a operação.
            print(f"Depósito no valor de R${deposito:.2f}\nRealizado com sucesso!")






	return saldo_atual + deposito

# LOOP WHILE TRUE DE OPÇÕES
atendimento = True	# CONTROLARÁ O LOOP ATÉ A MESMA SER DECLARADA COMO FALSE
while atendimento:
    operacao = menu_inicial()

# SAQUE
    if operacao == "1":
        print("######### Saque #########")
        valor = float(input("Digite o valor do saque:\n"))
        if valor < 0: #                         #Verifica se o valor digitado é negativo.
            print("Valor Inválido!")
        elif saques_diario == 0:                #Verifica se o limiti diário de saque foi atingido.
            print("Você atingiu o limite máximo de saques por dia, tente novamente amanhã!")
        elif valor > saldo_usuario:             #Verifica se o cliente tem saldo suficiente na conta
            print("Saldo insuficiente")
        elif valor > limite_por_saque:          #Verifica se o valor solicitado ultrapassa o limite por saque
            print("Limite de saque diario(R$ 500,00) excedido!\nTente outro valor")
        else:                                   # Passados todas as verificações realizará a operação
            saldo_usuario -= valor              # Debita o valor solicitado da conta do usuário.
            saques_diario -= 1                  #
            extrato += f"{contador_operacoes} - Saque no valor de: R${valor:.2f}\n"
            contador_operacoes += 1
            print(f"Saque no valor de {valor:.2f} Realizado!\nRetire o valor abaixo!")

            # Sub-Menu para verificar se o usuário deseja fazer outro procedimento ou sair do sistema
            outra_operacao = input(""" 
Deseja Realizar outra operacao?
		[1]- SIM
		[0]- NAO
			""")

            if outra_operacao == "0":
                print("Obrigado por utilizar nossos servicos")
                atendimento = False
            


# DEPOSITO
    elif operacao == "2":
        print("######### Deposito #########")
        deposito = float(input("Qual o valor R$ do depósito: \n")) # Coleta o valor solicitado

        if deposito < 0:    # Verifica se o valor é válido
            print("Valor inválido")
            print("Tente Novamente!")
        else:                               # Realiza a operação de depósito
            saldo_usuario += deposito       # Adiciona o valor a conta.
            extrato += f"{contador_operacoes} - Depósito no valor de R${deposito:.2f}\n" # Registra a operação no extrato.
            contador_operacoes += 1         # Registra a operação.
            print(f"Depósito no valor de R${deposito:.2f}\nRealizado com sucesso!")

        # Sub-Menu para verificar se o usuário deseja fazer outro procedimento ou sair do sistema
        outra_operacao = input("""
Deseja Realizar outra operacao?
		   [1] - SIM
		   [0] - NAO
        			""")

        if outra_operacao == "0":
            print("Obrigado por utilizar nossos servicos")
            atendimento = False
        

# EXTRATOS
    elif operacao == "3":
        print("########### Extrato ###########")    #Impressão do extrato.
        print("          Movimentações")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo atual é de: R${saldo_usuario:.2f}")

        outra_operacao = input("""
Deseja Realizar outra operacao?
		   [1] - SIM
		   [0] - NAO
                			""")

        # Sub-Menu para verificar se o usuário deseja fazer outro procedimento ou sair do sistema
        if outra_operacao == "0":
            print("Obrigado por utilizar nossos servicos")
            atendimento = False
        

# QUEBRA DO LOOP
    elif operacao == "0":
        print("Obrigado por utilizar nossos servicos")
        atendimento = False

    else:
        print("Opcao invalida, Tente Novamente!")

# FIM DO PROGRAMA.

def validar_nome_produto()-> str:
        while True:
            nome = input("Digite o nome do produto:\n").lower()
            if len(nome) == 0:
                print('Nome inválido, Nome não pode ser vazio, digite um nome válido')
                
            else:
                return nome
                
def validar_int(opcao = None) -> int:
    # Validar o retorno de um inteiro, recebe um parâmetro com padrão None, para diferenciar na mensagem de apresentada ao usuário
        if opcao == 'quantidade':
            while True:
                entrada = input("Digite a quantidade adquirida:\n")
                try:
                    inteiro = int(entrada)
                    return inteiro
                except ValueError: 
                    print('Digite um valor inteiro, Tente novamente')
        else:
            while True:
                entrada = input("Digite a opção desejada:\n")
                try:
                    inteiro = int(entrada)
                    return inteiro
                except ValueError: 
                    print('Digite um valor inteiro, Tente novamente')
            
    
def validar_valor_real() -> float:
        
        while True:
            entrada = input("Digite seu valor unitário em (R$) do produto:\n")
            try:
                valor = float(entrada)
                return valor
            except ValueError:
                print('Valor Incorreto\nDigite Novamente!')
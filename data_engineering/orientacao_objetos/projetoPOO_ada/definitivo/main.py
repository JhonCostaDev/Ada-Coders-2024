from classes.estoque import Estoque

def main():
    
    def menu():
        print(f'''
============== Controle de Estoque by Ada ===============
|               PRESSIONE UMA DAS OPÇÕES ABAIXO:        |
|                    1. VER ESTOQUE                     |
|                    2. CADASTRAR NOVO ITEM             |
|                    3. EXCLUIR PRODUTO                 |
|                    4. LIMPAR ESTOQUE                  |
|                    0. FINALIZAR                       |
=========================================================                    
''')
        # while True:
        #     entrada = input("Digite a opção desejada:\n")
        #     try:
        #         opcao = int(entrada)
        #         return opcao
        #     except ValueError: 
        #         print('Digite um valor inteiro, Tente novamente')
        opcao = validar_int()
        return opcao
        
    
    # Validar nome para nao receber valores vazios
    def validar_nome_produto():
        while True:
            nome = input("Digite o nome do produto:\n")
            if len(nome) == 0:
                print('Nome inválido, Nome não pode ser vazio, digite um nome válido')
                
            else:
                return nome
                
    # Validar o retorno de um inteiro
    def validar_int(opcao = None):
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
            
    
    def validar_valor_real():
        #TODO: implementar conversao do '.' para ','
        while True:
            entrada = input("Digite seu valor unitário do produto:\n")
            try:
                valor = float(entrada)
                return valor
            except ValueError:
                print('valor incorreto')
    
    # Cadastrar um novo produto        
    def cadastrar_produto():
        nome_produto = validar_nome_produto()
        valor = validar_valor_real()
        quantidade = validar_int('quantidade')
        Estoque(nome_produto, valor, quantidade)
        print("==============================")
        print('Produto cadastrado com sucesso')
        print("==============================")
    
    while True:
        inicio = menu()
        if inicio == 1:
            Estoque.exibir_estoque()
            
        elif inicio == 2:
            cadastrar_produto()
            
        elif inicio== 3:
            item = validar_nome_produto()
            Estoque.deletar_iten(item)
        elif inicio == 4:
            print("Tem certeza que deseja excluir todos os itens do estoque?\nDigite 0 - NÃO | 1 - SIM")
            opcao = validar_int()
            if opcao == 1:
                Estoque.limpar_estoque()
            else:
                print("Operação cancelada")
        elif inicio == 0:
            break
        else:
            print("=================================")
            print('Entrada inválida, tente novamente')
            print("=================================")
        
  
if __name__ == "__main__":
    main()
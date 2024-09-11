import os
import time
from validacao import *
from classes.estoque import Estoque

def limpar_tela()-> None:
# Essa função limpará o terminal(bash), melhorando a visibilidade
# Ela utiliza a biblioteca os na função system para identificar o sistema operacional
# e utilizar o comando correto.
    os.system('cls' if os.name =='nt' else 'clear')
    


    # Menu principal
def menu() -> int:
        limpar_tela()
        print(f'''
============== Controle de Estoque by Ada ===============
|               PRESSIONE UMA DAS OPÇÕES ABAIXO:        |
|                    1. VER ESTOQUE                     |
|                    2. MENU DE PRODUTOS                |
|                    3. LIMPAR ESTOQUE                  |
|                     0. FINALIZAR                      |
|                                                       |
=========================================================                    
''')
        opcao = validar_int()
        return opcao
    
    
def menu_produtos() -> int:
        # Menu de produtos
        limpar_tela()
        print(f'''
============== Controle de Estoque by Ada ===============
|               PRESSIONE UMA DAS OPÇÕES ABAIXO:        |
|                 1. CADASTRAR NOVO PRODUTO             |
|                 2. ALTERAR NOME DE UM PRODUTO         |
|                 3. ALTERAR VALOR DE UM PRODUTO        |
|                 4. EXCLUIR PRODUTO                    |
|                 0. VOLTAR AO MENU ANTERIOR            |
=========================================================                    
''')
        opcao = validar_int()
        return opcao
'''
     Funções de validação
'''   
    
    # Cadastrar um novo produto        
def cadastrar_produto() -> None:
        # Essa função será responsável por criar um novo Objeto, ela criar as variáveis necessária para o estânciamento do objeto utilizando funções de validação dos dados. e no fim cria o Objeto Estoque.
        nome_produto = validar_nome_produto()
        valor = validar_valor_real()
        quantidade = validar_int('quantidade')
        Estoque(nome_produto, valor, quantidade)
        
        time.sleep(3)
        
#=====================================================================================
def main() -> None:
    # Função principal utilizada para controlar as funcionalidades das classes e módulos
    while True:
        inicio = menu()
        if inicio == 1:
            Estoque.exibir_estoque()
            
        elif inicio == 2:
            opcao_produto = menu_produtos()
            if opcao_produto == 1:
                cadastrar_produto()
            elif opcao_produto == 2:
                nome_produto = validar_nome_produto()
                if Estoque.buscar_produto(nome_produto):
                    print("------- Novo nome ------- ")
                    novo_nome = validar_nome_produto()
                    Estoque.alterar_nome(nome_produto, novo_nome)
                else:
                    print("Produto não encontrado!")
                    time.sleep(1.8)
            elif opcao_produto == 3:
                nome_produto = validar_nome_produto()
                if Estoque.buscar_produto(nome_produto):
                    novo_valor = validar_valor_real()
                    Estoque.alterar_valor(nome_produto, novo_valor)
                else:
                    print("Produto não encontrado!")
                    time.sleep(1.8)
            elif opcao_produto == 4:
                nome_produto = validar_nome_produto()
                if Estoque.buscar_produto(nome_produto):
                    print(f"Tem certeza que deseja excluir {nome_produto} do estoque?\nDigite 0 - NÃO | 1 - SIM")
                    opcao = validar_int()
                    if opcao == 1:
                        Estoque.deletar_item(nome_produto)
                    else:
                        print("=================================")
                        print("     Operação cancelada")
                        print("=================================")
                        time.sleep(1.8)
                else:
                    print("Produto não encontrado!")
                    time.sleep(1.8)
            elif opcao_produto == 0:
                continue
            else:
                print("Opção Inválida")
                
            
            
        elif inicio== 3:
            print("Tem certeza que deseja excluir todos os itens do estoque?\nDigite 0 - NÃO | 1 - SIM")
            opcao = validar_int()
            if opcao == 1:
                Estoque.limpar_estoque()
                time.sleep(1.8)
            else:
                print("=================================")
                print("     Operação cancelada")
                print("=================================")
                time.sleep(1.8)
        
        elif inicio == 0:
            break
        else:
            print("=================================")
            print('Entrada inválida, tente novamente')
            print("=================================")
        
  
if __name__ == "__main__":
    main()
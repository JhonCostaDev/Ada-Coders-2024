def validar_valor_real():
    while True:
        entrada = input("Digite um valor em Real (formato: 1234,56): ")
        
        # Verifica se a entrada contém apenas números, pontos e vírgula
        if all(char.isdigit() or char in {'.', ','} for char in entrada):
            # Verifica se há exatamente uma vírgula
            if entrada.count(',') == 1:
                # Divide o número antes e depois da vírgula
                parte_inteira, parte_decimal = entrada.split(',')
                
                # Verifica se a parte decimal tem exatamente dois dígitos
                if len(parte_decimal) == 2:
                    # Remove os pontos da parte inteira e verifica se é numérica
                    parte_inteira_sem_pontos = parte_inteira.replace('.', '')
                    if parte_inteira_sem_pontos.isdigit():
                        valor_numerico = float(parte_inteira_sem_pontos + '.' + parte_decimal)
                        print(f"Valor válido: R$ {valor_numerico:,.2f}")
                        return valor_numerico
        
        print("Erro: Formato inválido. Tente novamente.")

# Exemplo de uso:
# valor = validar_valor_real()
# print(valor)

# def meu_validar_real():
#     while True:
#         entrada = input("digite\n")
#         try:
#             valor = float(entrada)
#             return valor
#         except ValueError:
#             print('valor incorreto')
            
    
            
            
            
# a = meu_validar_real()
# print(a)

frutas = {
    "maçã": [3.50, 10],  # [preço, quantidade]
    "banana": [2.00, 20],
    "laranja": [4.00, 15],
    "uva": [5.00, 8]
}
# print('___________________________________________________')
# print("|    Produto  |   Valor unitario  |   Quantidade  |")
# for chave, valor in frutas.items():
#     print(f'|{chave}         |       {valor[0]}         |    {valor[1]}         |\n---------------------------------------------------')
    
# print('___________________________________________________\n')

def imprimir_tabela(dicionario):
    # Cabeçalhos
    print("-" * 35)
    print(f"{'|Fruta':<10}  |{'Preço (R$)':<10} |{'Quantidade':<10} |")
    print("-" * 35)
    
    # Linhas da tabela
    for fruta, detalhes in dicionario.items():
        print(f"| {fruta:<10}| {detalhes[0]:<10}| {detalhes[1]:<10}|")
        
imprimir_tabela(frutas)
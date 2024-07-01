'''
Ex 2.2
Suponha que o preço de capa de um livro seja R$ 24.95, mas as livrarias recebem um
desconto de 40%. O transporte custa R$ 3.00 para o primeiro exemplar e R$ 0.75 para
cada exemplar adicional. Qual será o custo total de atacado para 60 cópias?
'''
quantidade = 60
valor_capa = 24.95
desconto_atacado = valor_capa * 0.4

total_livros = quantidade * (valor_capa - desconto_atacado)
print(f"Total Livros: R$ {total_livros:.2f}")


envio_unidade = 3.0
desconto_segunda_unidade = envio_unidade * 0.25
total_envio = envio_unidade + (desconto_segunda_unidade * (quantidade - 1))
print(f"Total Envio: R$ {total_envio:.2f}")

print(f"Custo Final: {total_livros + total_envio:.2f}")



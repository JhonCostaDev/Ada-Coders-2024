#%%
from modulos.produto import Produto
from modulos.estoque import Estoque

banana = Produto('Banana', 10, 1.99)
print(banana)

#TODO: Utilizar herança na minha classe estoque > produto
#TODO: Utilizar a aula de hoje para aprimorar o projeto/.

# e1 = Estoque()
# e1.exibir_estoque()
banana.quantidade = 15
banana.quantidade = 1
print(banana)



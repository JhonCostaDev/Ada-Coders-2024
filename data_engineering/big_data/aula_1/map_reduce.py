#%%
header = ['Nome_produto', 'Quantidade', 'Preco_unitario']
data = {
    'produto_a': [10, 5.0],
    'produto_b': [5, 7.5],
    'produto_a': [8, 5.0],
    'produto_c': [3, 12.],
    'produto_b': [2, 7.5],
    'produto_a': [12, 5.]
}

# %%
print(data)
# %%
for produto in data:
    print(data.get(produto))
# %%

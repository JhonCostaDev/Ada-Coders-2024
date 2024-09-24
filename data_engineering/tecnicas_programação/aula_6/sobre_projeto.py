# import pandas as pd 
# class analise_csv:
#     def __init__(self, arquivo):
#         self._arquivo = arquivo

import pandas as pd

class DataFrameInfo:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def exibir_info(self):
        print("Informações do DataFrame:")
        print(self.dataframe.info())
        print("\nPrimeiras linhas do DataFrame:")
        print(self.dataframe.head())
        print("\nEstatísticas descritivas:")
        print(self.dataframe.describe())

# Exemplo de uso
dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Daniela'],
    'Idade': [23, 35, 45, 28],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Fortaleza']
}

df = pd.DataFrame(dados)
info = DataFrameInfo(df)
info.exibir_info()


# seu dataset esta ocupando xMB de memoria do sistemaa
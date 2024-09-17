import pandas as pd
notas = pd.Series([10, 8, 6.5, 9, 7.5, 8.5, 9, 9, 4, 8.5, 7.5,8, 10, 10, 4.5, 4.5, 9, 8, 8, 9, 9, 9, 6.5,5, 6, 4.5, 9, 10, 1, 0,5, 7, 9, 6.5, 5, 8])

# A nota media
media = notas.mean()
# Desvio padrão
desvio = notas.std()
# A moda
moda = notas.mode()

# A mediana
mediana = notas.median()

print(f"""
#########################################
            Media: {media}
            Desvio Padrão: {desvio}
            Moda: {moda}
            Mediana = {mediana}
#########################################
""")

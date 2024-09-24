#%%
import pandas as pd 

df = pd.read_csv('../archive/BRK-A.csv')

# %%
df.describe()
# %%
df.info(memory_usage='deep')
# %%
df
# %%
df['Date']
# %%

#%%
import pandas as pd
import csv

#%%
df = pd.read_csv('jkw_no_double.csv')
#%%
df
#%%
df.drop_duplicates(subset=1, inplace=True)
del df[0]
df.columns = ['Tweet', 'Sentimen']
df.drop(0, inplace=True)

#%%
df
#%%
df.to_csv('pbw_no_double.csv')
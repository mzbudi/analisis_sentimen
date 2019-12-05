#%%
import pandas as pd
file_name = "jkw_no_jutsu.csv"
#%%
df = pd.read_csv(file_name)
#%%
df = df[df["Sentimen"] != 0]

#%%
df.drop_duplicates(subset="Tweet", inplace=True)
#%%
df.rename({"Unnamed: 0":"a"}, axis="columns",inplace=True)
#%%
del df["a"]

#%%
df.sort_index()
df.dropna(axis=0, inplace=True)
#%%
df.to_csv(file_name)

#%%

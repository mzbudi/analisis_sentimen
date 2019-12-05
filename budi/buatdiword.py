#%%
import pandas as pd 

df = pd.read_csv("poststem2.txt")

#%%
pos = []
with open("negstem2.txt") as f:
    lines = f.readlines()
    for line in lines:
        line = line.split(',')[0]
        pos.append(line)


#%%
pos
#%%
dfpos = pd.DataFrame({
    "Kata" : pos
})
#%%
dfpos.to_csv("katanegatip.csv")

#%%
dfpos1 = dfpos.iloc[0:100]
dfpos2 = dfpos.iloc[101:200]
dfpos3 = dfpos.iloc[201:300]

#%%
pos1 = []
for kata in dfpos1:
    print(dfpos1)

#%%
dfpos2 = pd.DataFrame({
    "Kata 1" : dfpos1,
    "Kata 2" : dfpos2,
    "Kata 3" : dfpos3
})
#%%

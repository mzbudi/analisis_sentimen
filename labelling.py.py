#%%
import pandas as pd
import re
from tqdm import tqdm_notebook as tqdm

#%%
pos = []
with open("poststem2.txt") as f:
    lines = f.readlines()
    for line in lines:
        line = line.split(',')[0]
        pos.append(line)

#%%
kata_kata = {kata:1 for kata in pos}

#%%
with open('budi/negstem2.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.split(',')[0]
        try:
            if kata_kata[line] != 1:
                kata_kata[line] = -1
        except KeyError:
            kata_kata[line] = -1

#%%
df = pd.read_csv('budi/stemmed_kpu_no_jutsu.csv')

#%%
del df['Unnamed: 0']
#%%
words = df['Stemmed']
#%%
def stem(ab):
    a = ab.split()
    a = [re.sub(r'(mem|kan|ter|per)', '', b) for b in a]
    return ' '.join(a)


#%%
for i, ws in enumerate(words):
    words.iloc[i] = stem(ws)

#%%
scores = []
for ws in tqdm(words):
    wss = ws.split()
    sc = 0
    i = 0
    for w in wss:
        try:
            sc += kata_kata[w]
            i += 1
        except:
            continue
    if i != 0:
        scores.append(sc/i)
    else:
        scores.append(0.0)
#%%
i = 0
for s in scores:
    if s == 0:
        i += 1

#%%
mask = scores != 0.0

#%%
scores = scores[mask]

#%%
import numpy as np

#%%
scores = np.array(scores)

#%%
for i, s in enumerate(scores):
    if s > 0:
        scores[i] = 1
    elif s < 0:
        scores[i] = -1
    else:
        scores[i] = 0

#%%
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV, train_test_split


#%%
vectorizer = TfidfVectorizer(min_df=0.01, max_df=3.0)
model = GridSearchCV(SVC(), {'gamma':[1, 0.1, 0.001, 0.0001, 0.00001],
                                         'kernel':['linear', 'rbf']},
                                 refit=True, verbose=0)

#%%
words_f = vectorizer.fit_transform(raw_documents=words)

#%%
x_train, x_test, y_train, y_test = train_test_split(words_f, scores,
                                                            test_size=0.2, shuffle=True)

#%%
model.fit(x_train, y_train)

#%%
model = model.best_estimator_

#%%
model.fit(x_train, y_train)

#%%
y_pred = model.predict(x_test)

#%%
report = classification_report(y_test, y_pred, output_dict=True)
report

#%%
scores
pd.DataFrame({
    "Tweet" : words,
    "Scores" : scores
}).to_csv("kpu_scored1.csv")

df1 = pd.DataFrame({
    "Tweet" : words,
    "Scores" : scores
})

df1 = df1[df1["Scores"] != 0.0]

df1

df1.to_csv("kpu_scored_no_netral.csv")

dfpos = pd.read_csv("kpu_scored_no_netral.csv")

dfpos.rename({"Unnamed: 0":"a"}, axis="columns",inplace=True)

del dfpos["a"]

dfpos = dfpos[dfpos["Scores"] != 1.0]

dfpos.to_csv("kpu_negatif.csv")

dfpos

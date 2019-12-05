#%%
import pandas as pd
import numpy as np 
import re
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(font_scale=1.2)
df = pd.read_csv("kpu_scored_no_netral_coba.csv")
df

#%%
dfloc = df.iloc[0:1000]
dfloc.rename({"Unnamed: 0":"a"}, axis="columns",inplace=True)

del dfloc["a"]
#%%
dfneg = dfloc[dfloc["Scores"] != 1]
dfneg.to_csv("data2negatif_fix.csv")

#%%
dfpos = dfloc[dfloc["Scores"] != -1]
dfpos.to_csv("data2positif_fix.csv")

#%%
words = dfloc["Tweet"]
scores = dfloc["Scores"]
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


#%%
report

#%%
dfpos["Tweet"]

#%%
dfloc.to_csv("1000data.csv")

#%%

y_pred
#%%

words = pd.DataFrame(df["Tweet"])
#%%
words.to_csv("tokenizer.txt")
#%%
token = []
with open("tokenizer.txt") as t:
    lines = t.readlines()
    for line in lines:
        
        print(line)



#%%
twit = []
sentimen = []
for idx in y_test.index:
    twit.append(words[idx])
    sentimen.append(scores[idx])

#%%
dfapaini = pd.DataFrame({
    "Tweet" : twit,
    "Score" : sentimen,
    "Prediksi" : y_pred
})
#%%
dfapaini.to_csv("Hasil_prediksi.csv")

#%%

#%%

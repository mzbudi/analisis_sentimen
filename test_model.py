#%%
import pandas as pd
import joblib
from sklearn.svm import SVC

#%%
test_data = joblib.load("kpu_Test_datas.data")
model = joblib.load("kpu_classifier.svm")
#%%
hasil = model.predict(test_data["TFIDF"])
#%%
df = pd.DataFrame({
    "Tweet": test_data["Tweet"],
    "Label": test_data["Sentimen"],
    "Prediksi": hasil
})

#%%
df

#%%

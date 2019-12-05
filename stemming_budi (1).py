from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
import spacy
import pandas as pd
from tqdm import tqdm
remover = StopWordRemoverFactory().create_stop_word_remover()
tokener = spacy.blank("id")
def stem_and_remove(ws):
    temp = ""
    ws = tokener(ws)
    for w in ws:
        temp += "%s "%w.lemma_.strip()
        temp = remover.remove(temp)
    return temp

sw = open("stopwords.txt", 'r')
_sw = sw.readlines()
for i, s in enumerate(_sw):
    _sw[i] = s.strip()

remover.dictionary.add_words(_sw)
#if remover.dictionary.contains("yuhu"):
#    print('exist')
sw.close()
#file_name = ["pbw", "jkw"]
file_name = ['kpu']
for fn in file_name:
    filename = "stemmed_%s_no_jutsu.csv"%fn
    #original = "%s_no_jutsu.csv"%fn
    #filename = "%s_mau_di_stemfix.csv"%fn
    df = pd.read_csv(filename)
    #df_ori = pd.read_csv(original)
    #print(len(df_ori["Tweet"]))
    print(len(df["Tweet"]))
    df["Tweet"] = df["Tweet"].str.replace("\d+", "")
    tweets = []
    tweets_ori = []
    for tw in tqdm(df["Tweet"]):
        clean_tw = stem_and_remove(tw)
        _tw = clean_tw.split(" ")
        if len(_tw) >= 4:
            try:
                tweets.append(clean_tw)
                #tweets_ori.append(df_ori["Tweet"][i])
            except Exception:
                continue
            
    pd.DataFrame({
        "Stemmed": tweets,
    }).to_csv("stemmed_%s_no_jutsu.csv"%fn)
    print("Done %s"%filename)

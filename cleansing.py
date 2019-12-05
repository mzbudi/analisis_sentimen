import re
from pandas import DataFrame

def clean(idx, text):
    text = text.strip()
    try:
        text = text.split('%d_efw7912jdqw['%idx)[1]
    except:
        pass
    text = text.split(']_932ruo')
    if len(text) == 2:
        idx += 1
    text = text[0]
    text = re.sub(r"http\S+", '', text)
    text = re.sub(r"#\S+", '', text)
    text = re.sub(r"RT @[^\s]+:", '', text)
    text = re.sub(r"@", '', text)
    text = re.sub(r"[^0-9a-zA-Z ]+", '', text)
    text = re.sub(r"RT dan reply.*$", '', text).lower().rstrip()
    return idx, text

df = DataFrame(columns=['Tweet'])
idx = 0
concat = False
with open('kpu1.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        if not line.isspace():
            last_idx = idx
            if concat:
                idx, next_text = clean(last_idx, line)
                text += ' '+next_text
            else:
                idx, text = clean(last_idx, line)
            if last_idx == idx:
                concat = True
            else:
                concat = False
                print(idx)
                df = df.append({'Tweet': text}, ignore_index=True)

df.to_csv(r"kpu1.csv")

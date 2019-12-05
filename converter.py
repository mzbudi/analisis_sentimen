#%%
import csv

with open('list_words.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('list_words.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('words', 'sampah'))
        writer.writerows(lines)

#%%

import json

out = open('kpu3.txt', 'w')
with open('kpu3.json', 'r') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        j_line = json.loads(line)
        out.writelines('%d_124qdeq[%s]$_12eqd\n'%(i, j_line['text']))
        print(i)
out.close()
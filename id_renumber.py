# id_renumber.py
# py id_renumber.py <link.edgelist> <diffusion> <output path(conversion table)>
# idを1から振り直す

import sys
from collections import defaultdict

argv = sys.argv
link = argv[1]
diffusion = argv[2]
output = argv[3]


# idの変換テーブルを作る
idset = set()
conversion_table = defaultdict(int)
link_data = []
for line in open(link):
    sp = line.strip().split(" ")
    idset.add(int(sp[0]))
    idset.add(int(sp[1]))
    link_data.append(line) #リンクの中身をコピーしておく

dif_data = []
for line in open(diffusion):
    dif_data.append(line)

idlist = sorted(list(idset))
#print(idlist)
count = 1
for id in idlist:
    if conversion_table[id] == 0:
        conversion_table[id] = count
        count += 1
    

        
with open(link,"w") as f:
    for line in link_data:
        sp = line.strip().split(" ")
        f.write("{} {}\n".format(conversion_table[int(sp[0])],conversion_table[int(sp[1])]))

with open(diffusion,"w") as f:
    for line in dif_data:
        sp = line.strip().split(" ")
        f.write("{} {}\n".format(conversion_table[int(sp[0])],sp[1]))

with open(output,"w") as f:
    for k,v in sorted(conversion_table.items()):
        f.write("{} {}\n".format(k,v))

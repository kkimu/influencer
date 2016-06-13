# id_renumber.py
# py id_renumber_Twitter-follow.py
# idを1から振り直す

import time
import sys
from collections import defaultdict

for n in range(1,101):
    t1 = time.time()
    link = "./Twitter-follow/data/link_{}.txt".format(n)
    diffusion = "./Twitter-follow/data/diffusion_result_{}.txt".format(n)
    idl = "./Twitter-follow/data/idlist_{}.txt".format(n)
    output = "./Twitter-follow/data/conversion_table_{}.txt".format(n)
    
    # idの変換テーブルを作る
    idset = set()
    conversion_table = defaultdict(int)
    for line in open(idl):
        idset.add(int(line.strip()))

    dif_data = []
    for line in open(diffusion):
        dif_data.append(line)
    link_data = []
    for line in open(link):
        link_data.append(line)

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

    with open(idl,"w") as f:
        for id in idlist:
            f.write("{}\n".format(conversion_table[id]))
            
    with open(output,"w") as f:
        for k,v in sorted(conversion_table.items()):
            f.write("{} {}\n".format(k,v))

    print("Time:{}".format(time.time()-t1))

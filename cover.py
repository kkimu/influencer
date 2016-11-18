# リツイート数上位1%のノードをどれだけカバーしているか
# 

import time
from collections import defaultdict
import sys
import os


t0 = time.time()
argv = sys.argv
dataset = str(argv[1])
#top = int(argv[2])

cover = [1,2,3,4,5,6,7,8,9,10,12,15,20,30,40,50,60,70,80,90] 
    
indices = ["deg","pr","kcore","clo","bet"]

# リツイート数による正解ランキングをrt_rankに入れる
rt_rank = []
rt_num = defaultdict(int)
overlap = 0


if dataset != "Twitter-follow":
    dif_path = "{}/data/diffusion_result.txt".format(dataset)
    el_path = "{}/data/link.edgelist".format(dataset)

    idset = set()
    for line in open(el_path):
        sp = line.strip().split(" ")
        idset.add(sp[0])
        idset.add(sp[1])
    idlen = len(idset)
    top = round(idlen / 100)
else:
    dif_path = "{}/data/diffusion_result_1.txt".format(dataset)
    idlen = 50000
    top = 500

for line in open(dif_path):
    sp = line.strip().split(" ")
    rt_rank.append(sp[0])
    rt_num[sp[0]] = sp[1]

    
print("Inpup RT rank. time:{}".format(time.time()-t0))


rank = defaultdict(list)
for i in indices:
    path = "analysis/{}_{}.list".format(dataset, i)
    for line in open(path):
        sp = line.strip().split(" ")
        rank[i].append(sp[0])

print("Input estimated rank time:{}".format(time.time()-t0))

rt_top_set = set(rt_rank[:top]) #リツイートのランキング上位1%のノードの集合を作成

with open("analysis/cover_{}.csv".format(dataset),"w") as f:
    f.write("Cover 1%,Degree,PageRank,Closeness,Betweenness,kcore\n")
    for c in cover:
        f.write("{}%".format(c))
        p = round(idlen / 100 * c)
        for i in indices:
            cover_set = set(rank[i][:p])
            f.write(",{}".format((top - len(rt_top_set - cover_set)) / top))
        f.write("\n")

        print("Cover{} time:{}".format(p, time.time() - t0))

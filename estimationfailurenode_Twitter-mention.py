# 影響力の強いノード推定に失敗したノードはどういうノードなのか
# 

import time
from collections import defaultdict
import sys
import os


t0 = time.time()
argv = sys.argv
dataset = str(argv[1])
#top = int(argv[2])

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
    top = round(len(idset) / 100)
else:
    dif_path = "{}/data/diffusion_result_1.txt".format(dataset)
    top = 500

for line in open(dif_path):
    sp = line.strip().split(" ")
    rt_rank.append(sp[0])
    rt_num[sp[0]] = sp[1]

    
    
print("import RT rank time={}".format(time.time()-t0))

# 次数中心性で推定したランキングをdeg_rankに入れる
deg_rank = []
deg = defaultdict(int)
deg_path = "analysis/{}_deg.list".format(dataset)
for line in open(deg_path):
    sp = line.strip().split(" ")
    deg_rank.append(sp[0])
    deg[sp[0]] = sp[1]

# PageRankで推定したランキングをpr_rankに入れる
pr_rank = []
pr = defaultdict(int)
pr_path = "analysis/{}_pr.list".format(dataset)
for line in open(pr_path):
    sp = line.strip().split(" ")
    pr_rank.append(sp[0])
    pr[sp[0]] = sp[1]

# 近接中心性で推定したランキングをclo_rankに入れる
clo_rank = []
clo = defaultdict(int)
clo_path = "analysis/{}_clo.list".format(dataset)
for line in open(clo_path):
    sp = line.strip().split(" ")
    clo_rank.append(sp[0])
    clo[sp[0]] = sp[1]

# 媒介中心性で推定したランキングをdeg_rankに入れる
bet_rank = []
bet = defaultdict(int)
bet_path = "analysis/{}_bet.list".format(dataset)
for line in open(bet_path):
    sp = line.strip().split(" ")
    bet_rank.append(sp[0])
    bet[sp[0]] = sp[1]

    

print("import estimated rank time={}".format(time.time()-t0))

#rt_rank_set = set
#rank_set = set
rt_rank_set = set(rt_rank[:top])
deg_rank_set = set(deg_rank[:top])
    
failednodes = rt_rank_set - deg_rank_set
    
out = []
for node in failednodes:
    rt_ranki = rt_rank.index(node)
    
    if node in deg_rank:
        deg_ranki = deg_rank.index(node)
        pr_ranki = pr_rank.index(node)
        clo_ranki = clo_rank.index(node)
        bet_ranki = bet_rank.index(node)
        
        degree = deg[node]
        pagerank = pr[node]
        closeness = clo[node]
        betweenness = bet[node]
    else:
        rt_ranki = len(rt_rank) + 1
        deg_ranki = len(deg_rank) + 1
        pr_ranki = len(pr_rank) + 1
        clo_ranki = len(clo_rank) + 1
        bet_ranki = len(bet_rank) + 1
        
        degree = ""
        pagerank = ""
        closeness = ""
        betweenness = ""
        
    #print("{0:7d}  correct rank = {1:4d}, degree rank = {2:4d}, pagerank rank = {3:4d}, degree = {4}, pagerank = {5}".format(int(node),rt_ranki, deg_ranki, pr_ranki, degree, pagerank))
    out.append("{},{},{},{},{},{},{},{},{},{}\n".format(node,rt_ranki,deg_ranki,pr_ranki,clo_ranki,bet_ranki,degree,pagerank,closeness,betweenness))
        
with open("analysis/{}_failednodes_top{}.csv".format(dataset,top),"w") as f:
    f.write("node,correct rank,degree rank,pagerank rank,closeness rank,betweenness rank,degree,PageRank,closeness,betweenness\n")
    f.writelines(out)
print("top{} time = {}".format(top, time.time() - t0))

#再帰的ノイズ除去した結果のOverlapを計算
#N回分の結果の平均
#gnuplot用


from collections import defaultdict
import sys
import os

#cent = ["deg","pr","clo","ci"]
cent = ["deg","pr"]
result = defaultdict(lambda : defaultdict(lambda : defaultdict(int)))
ave = defaultdict(lambda : defaultdict(int))

argv = sys.argv
dataset = str(argv[1])
n1 = int(argv[2])
n2 = int(argv[3])
t = int(argv[4])
tN = int(argv[5])
index = str(argv[6])
#リツイート数による正解のランキングをrt_rankに入れる
rt_rank = []
rt_num = defaultdict(int)
overlap = 0

if dataset != "Twitter-follow":
    dif_path = "{}/data/diffusion_result.txt".format(dataset)
    for line in open(dif_path):
        sp = line.strip().split(" ")
        rt_rank.append(sp[0])

    idset = set()
    for line in open("{}/data/link.edgelist".format(dataset)):
        sp = line.strip().split(" ")
        idset.add(sp[0])
        idset.add(sp[1])
    overlap = round(len(idset)*0.01)

print("overlap{}".format(overlap))
    
out_path = "./result_noise_reduction"
if os.path.exists(out_path) == False:
    os.makedirs(out_path)
    
for n in range(n1,n2+1):
    if dataset == "Twitter-follow":
        dif_path = "{}/data/diffusion_result_{}.txt".format(dataset,n)
        for line in open(dif_path):
            sp = line.strip().split(" ")
            rt_rank.append(sp[0])
            rt_num[sp[0]] = sp[1]

        idset = set()
        for line in open("{}/data/idlist_{}.txt".format(dataset,n)):
            idset.add(line.strip)
        overlap = round(len(idset)*0.01)
        print("ovrelap",overlap)

    for tn in range(0,tN+1):
        for c in cent:
            rank = []
            for line in open("./{}/noise_reduction/{}/{}_T{}_tn{}_{}.rank".format(dataset,n,index, t,tn,c)):
                rank.append(line.split(" ")[0])
        
            result[n][tn][c] = (len(set(rank[:overlap]) & set(rt_rank[:overlap]))/overlap)
            print("len(set(rank[:overlap]))={}, len(set(rt_rank[:overlap]))={}".format(len(set(rank[:overlap])),len(set(rt_rank[:overlap]))))
            print("n={},tn={},c={},result[n][tn][c]={}".format(n,tn,c,result[n][tn][c]))

    #出力
    with open("{}/{}_{}_T{}_n{}.csv".format(out_path, dataset, index ,t,n),"w") as f:
        f.write("#{} T{}%\n#Overlap1%,Degree,PageRank,Closeness,CI\n".format(index, t))
        for tn in range(0,tN+1):
            f.write(str(tn))
            for c in cent:
                f.write(",{}".format(result[n][tn][c]))
            f.write("\n")

for tn in range(0,tN+1):
    for c in cent:
        sum = 0
        for n in range(n1, n2+1):
            sum += result[n][tn][c]
        ave[tn][c] = sum/(n2-n1+1)


with open("{}/{}_{}_T{}.csv".format(out_path,dataset, index, t),"w") as f:
    f.write("#{} T{}%\n#Overlap1%,Degree,PageRank,Closeness,CI\n".format(index, t))
    for tn in range(0,tN+1):
        f.write(str(tn))
        for c in cent:
            f.write(",{}".format(ave[tn][c]))
        f.write("\n")

         
"""
for n in range(n1,n2+1):
    for c in cent:
        #100perのときのランキングを入れる
        rank100 = []
        for line in open("./{}/noise_reduction/{}/tn{}_.txt".format(dataset,n,tn,c)):
             rank100.append(line.strip().split(" ")[0])
        
        for tn in range(0,tn+1):
            ###rankに順位を入れる
            for p in per:
                if(p == 100):
                    for o in overlap:
                        result[n][s][c][o].append(len(set(rank100[:o]) & set(rt_rank[:o]))/o)
                else:
                    rank = []
                    for line in open("{}/result/{}/{}_{}_{}per.txt".format(dataset,n,s,c,p)):
                        rank.append(line.strip().split(" ")[0])
                    #Overlap p
                    for o in overlap:
                        result[n][s][c][o].append(len(set(rank[:o]) & set(rt_rank[:o]))/o)
    print(n)

for n in range(1,N+1):
    for s in sampling:
        for c in cent:
            for o in overlap:
                f = open("{}/overlap/{}/{}_{}_{}.txt".format(dataset,n,s,c,o),"w")
                for p in per:
                    f.write("{}\n".format(result[n][s][c][o][per.index(p)]))
                f.close                

ave = defaultdict(lambda: defaultdict(lambda: defaultdict(dict)))
out = []
for s in sampling:
    for c in cent:
        for p in per:
            for o in overlap:
                sum = 0
                for n in range(1,N+1):
                    sum += result[n][s][c][o][per.index(p)]
                ave[s][c][o][per.index(p)] = sum/N



for o in overlap:
    for s in sampling:
        f = open("{}/result/overlap{}_{}.csv".format(dataset,o,s),"w")
        f.write("#{}\n#Overlap{},Degree,PageRank,k-core\n".format(s,o))
        for p in per:
            f.write("{}".format(p))
            for c in cent:
                f.write(",{}".format(ave[s][c][o][per.index(p)]))
            f.write("\n")
    #f.write("\n")
"""

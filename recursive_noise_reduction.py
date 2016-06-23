# recursive_noise_reduction.py
# 
# 再帰的にノイズを除去し、各段階で指標を求める

import time
import os
import random
import sys
import subprocess
import gc
from collections import defaultdict

def recursive(dataset, n1, n2, t, tn, index):
    t0 = time.time()
    directed = True

    # データセットがFacebookかAPSならdirectedにFalseを設定
    if dataset == "Facebook" or dataset == "APS":
        directed = False
        
    for n in range(n1,n2+1):
        
        t1 = time.time()

        # データセットがTwitter-follow以外ならlink pathを設定
        if dataset != "Twitter-follow":
            link_path = "./{}/data/link".format(dataset)
            idset = set()
            for line in open("{}.edgelist".format(link_path)):
                sp = line.strip().split(" ")
                idset.add(int(sp[0]))
                idset.add(int(sp[1]))
            print("len(idset) = {}".format(len(idset)))
            idlen = len(idset)
                
        # データセットがTwitter-followならlinkとidlistを別で設定
        elif dataset == "Twitter-follow":
            link_path = "./Twitter-follow/data/link_{}".format(n)
            idset = set()
            for line in open("./Twitter-follow/data/idlist_{}.txt".format(n)):
                idset.add(line.strip())
            print("len(idset) = {}".format(len(idset)))
            idlen = len(idset)
            
         # 出力するpathを設定
        out_path = "./{}/noise_reduction/{}".format(dataset, n)
        # ディレクトリがなければ作る
        if os.path.exists(out_path) == False:
            os.makedirs(out_path)

        # 再帰的にノイズ除去する回数tn 繰り返す
        for tn in range(0,tn+1):
            t2 = time.time()

            print("################################################")
            print("n={}, tn={}".format(n,tn))
            print("################################################")

            
            ### 影響力の指標を計算する
            # 次数中心性、PageRank、近接中心性
            if dataset == "Twitter-mention" or dataset == "APS":
                cmd = "R --vanilla --slave --args {}.edgelist {}/{}_T{}_tn{}_ {} < c_deg_pr.R >log/c_{}_{}_T{}_tn{}.log".format(link_path, out_path, index, t, tn, directed, dataset, index, t, tn)
            else:
                cmd = "R --vanilla --slave --args {}.edgelist {}/{}_T{}_tn{}_ {} < c_deg_clo_pr.R >log/c_{}_{}_T{}_tn{}.log".format(link_path, out_path, index, t, tn, directed, dataset, index, t, tn)
                
            print("Start '",cmd,"'",sep="")
            ret = subprocess.check_output(cmd,shell=True)
            print("End")

            # CI
            if dataset == "Twitter-follow" or dataset == "Facebook":
                 # adjacency listを出力
                adjacency_list("{}.edgelist".format(link_path), "{}.adjacencylist".format(link_path), directed)
                print("New adjacency list is created at {}.adjacencylist".format(link_path))
            
                cmd = "./CI_output {}.adjacencylist 3 {}/{}_T{}_tn{}_ci.rank >log/c_{}_{}_T{}_tn{}_CI.log".format(link_path,out_path, index, t, tn, dataset, index, t, tn)
                print("Start '",cmd,"'",sep="")
                ret = subprocess.check_output(cmd,shell=True)
                print("End")

            
            #指定した指標で計算した結果をrankに入れる
            rank = []
            if index == "ci":
                for line in open("{}/{}_T{}_tn{}_ci.rank".format(out_path, index, t, tn)):
                    sp = line.split(" ")
                    if len(sp) == 3:
                        rank.append(int(sp[1]))
            else:
                for line in open("{}/{}_T{}_tn{}_{}.rank".format(out_path, index, t, tn, index)):
                    rank.append(int(line.split(" ")[0]))
            
            # 計算に含まれなかったノードをランキングの後ろに追加
            #if dataset == "Twitter-follow":
            idlist = list(idset)
            random.shuffle(idlist)
            for id in idlist:
                if len(rank) >= idlen:
                    break
                if id not in rank:
                    rank.append(id)
            print("Padding ranking")

            
            # 下位T%のノードを削除したid集合を得る
            ranklen = len(rank)
            idlen_new = int(ranklen*t*0.01)
            del rank[ranklen-idlen_new:ranklen]
            idset = set(rank)
            idlen = len(idset)
            print("ranklen={}, idlen_new={}, len(rank)={}".format(ranklen, idlen_new, len(rank)))

            # 新しいid集合のネットワークを抽出
            lines = []
            for line in open("{}.edgelist".format(link_path)):
                sp = line.strip().split(" ")
                # 新しいid集合に含まれるid間のエッジのみを取得
                if int(sp[0]) in idset and int(sp[1]) in idset:
                    lines.append(line)
            # 出力先
            link_path = "./{}/noise_reduction/{}/data/reducted_{}_T{}_tn{}".format(dataset, n, index, t, tn+1)
            # ディレクトリがなければ作る
            if os.path.exists("./{}/noise_reduction/{}/data".format(dataset, n)) == False:
                os.makedirs(link_path)
            # edgelistを出力
            with open("{}.edgelist".format(link_path),"w") as f:
                f.writelines(lines)
            print("New edgelist is created at {}".format(link_path))

            
            print("tn = {}\tTime:{}\n".format(tn, time.time()-t2))

        print("n = {}\tTime:{}".format(n, time.time()-t1))

    print("Total Time:{}".format(time.time()-t0))
    
            
def adjacency_list(input,output,directed):
    max = 0
    al = defaultdict(set)
    for line in open(input):
        sp = line.strip().split(" ")
        id0 = int(sp[0])
        id1 = int(sp[1])
        if directed == True:
            al[id0].add(id1)
        elif directed == False:
            al[id0].add(id1)
            al[id1].add(id0)
        if max < id0:
            max = id0
        if max < id1:
            max = id1

    with open(output,"w") as f:
        for id in range(1,max+1):
            f.write(str(id))
            if al[id] != None:
                alist = list(al[id])
                for id2 in sorted(alist):
                    f.write(" {}".format(id2))
            f.write("\n")
        
                
if __name__ == "__main__":
    argv = sys.argv
    dataset = str(argv[1])
    n1 = int(argv[2])
    n2 = int(argv[3])
    t = int(argv[4])
    tn = int(argv[5])
    index = str(argv[6])
    recursive(dataset, n1, n2, t, tn, index)


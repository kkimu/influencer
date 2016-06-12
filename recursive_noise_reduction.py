# recursive_noise_reduction.py
# 
# 再帰的にノイズを除去し、各段階で指標を求める

import time
import os
import random
import sys
import subprocess

def recursive(dataset, n1, n2, t, tn):
    t0 = time.time()
    directed = True

    # データセットがFacebookかAPSならdirectedにFalseを設定
    if dataset == "Facebook" or dataset == "APS":
        directed = False
        
    for n in range(n1,n2+1):
        
        t1 = time.time()

        # データセットがTwitter-follow以外ならlink pathを設定
        if dataset != "Twitter-follow":
            link_path = "./{}/data/link.txt".format(dataset)
        # データセットがTwitter-followならlinkとidlistを別で設定
        elif dataset == "Twitter-follow":
            link_path = "./Twitter-follow/data/link_{}.txt".format(n)
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

            ### 影響力の指標を計算する
            # 次数中心性、PageRank、近接中心性
            cmd = "R --vanilla --slave --args {} {}/T{}_tn{}_ {} < c_deg_clo_pr.R".format(link_path, out_path, t, tn, directed)
            print("Start '",cmd,"'",sep="")
            ret = subprocess.check_output(cmd,shell=True)
            print("End")

            # CI
            cmd2 = "./CI {}.adjacencylist".format(link_path)
            ret

            #次数で計算した結果をrankに入れる
            rank = []
            for line in open("{}/T{}_tn{}_deg.rank".format(out_path, t, tn)):
                rank.append(line.split(" ")[0])
                
            # 計算に含まれなかったノードをランキングの後ろに追加
            if dataset == "Twitter-follow":
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
            for line in open(link_path):
                sp = line.strip().split(" ")
                # 新しいid集合に含まれるid間のエッジのみを取得
                if sp[0] in idset and sp[1] in idset:
                    lines.append(line)
            link_path = "./{}/data/reducted_deg_{}.edgelist".format(dataset, tn+1)
            with open(link_path,"w") as f:
                f.writelines(lines)
            print("New edgelist is created at {}".format(link_path))

            print("tn = {}\tTime:{}".format(tn, time.time()-t2))

        print("n = {}\tTime:{}".format(n, time.time()-t1))

    print("Time:{}".format(n, time.time()-t0))    
            
            
            
                
if __name__ == "__main__":
    argv = sys.argv
    dataset = str(argv[1])
    n1 = int(argv[2])
    n2 = int(argv[3])
    t = int(argv[4])
    tn = int(argv[5])
    recursive(dataset, n1, n2, t, tn)


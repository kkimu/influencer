# sampling.py
# py sampling.py <dataset name> <n1> <n2> <method> [number of seed nodes]
# datasetのネットワークからサンプリングする

import time
import os
from collections import defaultdict
import random
import sys
from operator import itemgetter

percent = [1, 2, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90] #サンプリングレート
#percent = [1]

def rand(dataset, n1, n2):
    t0 = time.time()
    t1 = time.time()
    
    # データセットがTwitter-follow以外なら、./{dataset}/data/link.txtを使う
    if dataset != "Twitter-follow":
        link_path = "./{}/data/link.txt".format(dataset)
        idlist = get_id_list(link_path)
        idlen = len(idlist)

        print("id number = {}\tTime:{}".format(idlen, time.time()-t1))
    
    for n in range(n1, n2+1):
        # データセットがTwitter-followなら、./Twitter-follow/data/link_{n}.txtを使う
        if dataset == "Twitter-follow":
            t1 = time.time()
            link_path = "./{}/data/link_{}.txt".format(dataset,n)
            idlist = get_id_list(link_path)
            idlen = len(idlist)
            print("{} id number = {}\tTime:{}".format(link_path, idlen, time.time()-t1))

        # 取得する割合%ごとに繰り返し
        for p in percent:
            t1 = time.time()
            num = int(idlen*p*0.01) # 取得するノード数
            random.shuffle(idlist)

            # 取得するノードを選択
            target_id = select_rand(num, idlist)
            print(len(target_id),"\t",end="")

            # パスとファイル名を指定して出力
            path = "{}/sampling/{}".format(dataset, n)
            filename = "rand_{}per".format(p)
            output(path, filename, link_path, target_id)

            
            print("Time_{}per_{}:{}".format(p,n,time.time() -t1))
        print("Time_{}:{}".format(n,time.time() -t0))

# 幅優先探索
def bfs(dataset, n1, n2, seednum):
    t0 = time.time()
    t1 = time.time()
    
    # データセットがTwitter-follow以外なら、./{dataset}/data/link.txtを使う
    if dataset != "Twitter-follow":
        link_path = "./{}/data/link.txt".format(dataset)
        idlist,al = get_id_list_and_adjacency_list(link_path)
        idlen = len(idlist)

        print("id number = {}\tTime:{}".format(idlen, time.time()-t1))
    
    for n in range(n1, n2+1):
        # データセットがTwitter-followなら、./Twitter-follow/data/link_{n}.txtを使う
        if dataset == "Twitter-follow":
            t1 = time.time()
            link_path = "./{}/data/link_{}.txt".format(dataset,n)
            idlist,al = get_id_list_and_adjacency_list(link_path)
            idlen = len(idlist)
            print("{} id number = {}\tTime:{}".format(link_path, idlen, time.time()-t1))

        # 取得する割合%ごとに繰り返し
        for p in percent:
            t1 = time.time()
            num = int(idlen*p*0.01) # 取得するノード数
            random.shuffle(idlist)

            # 取得するノードを選択
            target_id = select_bfs(num, idlist, al, seednum)
                
            print(len(target_id),"\t",end="")


            # パスとファイル名を指定して出力
            path = "{}/sampling/{}".format(dataset, n)
            filename = "bfs_{}per_seed{}".format(p,seednum)
            output(path, filename, link_path, target_id)

            
            print("Time_{}per_{}:{}".format(p,n,time.time() -t1))
        print("Time_{}:{}".format(n,time.time() -t0))

# idリスト全体からnumだけノードを選択する
def select_rand(num, idlist):
    target_id = defaultdict(int)
    for j in range(0, num):
        target_id[idlist[j]] = 1

    return target_id

# 幅優先探索でidリスト全体からnumだけノードを選択する
def select_bfs_old(num, idlist, al):
    target_id = defaultdict(int)
    random.shuffle(idlist)
    queue = []
    idnum = 0
    index = 0
    while idnum < num:
        if len(queue) == 0:
            for index2 in range(index,len(idlist)):
                if target_id[idlist[index2]] != 1:
                    target_id[idlist[index2]] = 1
                    queue.append(idlist[index2])
                    idnum += 1
                    index += 1
                    break
                else:
                    index += 1
        else:
            node = queue.pop(0)
            if len(al[node]) >= 1:
                for nei in al[node]:
                    if idnum < num:
                        if target_id[nei] != 1:
                            target_id[nei] = 1
                            idnum += 1
                            queue.append(nei)
                    else:
                        break

    return target_id

# 幅優先探索 複数のシードノードを用いる場合
def select_bfs(num, idlist, al, seednum):
    target_id = defaultdict(int)
    random.shuffle(idlist)
    queue = []*seednum
    for i in range(0,seednum):
        queue.append([])
    
    idnum = 0
    while idnum < num:
        for i in range(0,seednum):
            if idnum < num:
                if len(queue[i]) == 0:
                    node = random.choice(idlist)
                    while target_id[node] == 1:
                        node = random.choice(idlist)
                        
                    target_id[node] = 1
                    queue[i].append(node)
                    idnum += 1
                    
                else:
                    node = queue[i].pop(0)
                    if len(al[node]) >= 1:
                        for nei in al[node]:
                            if idnum < num:
                                if target_id[nei] != 1:
                                    target_id[nei] = 1
                                    idnum += 1
                                    queue[i].append(nei)
                            else:
                                break
            else:
                break
            
    return target_id    


# pathのエッジリストからidの集合を得る
def get_id_list(path):
    idset = set()
    for line in open(path):
        sp = line.strip().split(" ")
        idset.add(sp[0])
        idset.add(sp[1])

    return list(idset)

# pathのエッジリストからidの集合と隣接ノードが入ったハッシュを得る
def get_id_list_and_adjacency_list(path):
    idset = set() # idの集合
    al = defaultdict(list) # 隣接ノードが入ったハッシュ keyがノード、valueがその隣接ノード
    for line in open(path):
        sp = line.strip().split(" ")
        al[sp[0]].append(sp[1])
        idset.add(sp[0])
        idset.add(sp[1])

    # 隣接ノードの
    for k,v in al.items():
        random.shuffle(al[k])
    
    return (list(idset),al)

        
def output(path, filename, link_path, target_id):
    # ディレクトリがなければ作る
    if os.path.exists(path) == False:
        os.makedirs(path)

    # 選択したIDのリストを出力
    with open("{}/{}.idlist".format(path, filename), "w") as f:
        for k,v in target_id.items():
            f.write("{}\n".format(k))

    # 選択したIDに関するエッジリストを出力
    lines = []
    for line in open(link_path):
        sp = line.strip().split(" ")
        if(sp[0] in target_id and sp[1] in target_id):
            lines.append(line)
    with open("{}/{}.edgelist".format(path, filename), "w") as f:
        f.writelines(lines) 



if __name__ == "__main__":
    argv = sys.argv
    dataset = str(argv[1])
    n1 = int(argv[2])
    n2 = int(argv[3])
    method = str(argv[4])

    if len(argv) < 6:
        seednum = 1
    else:
        seednum = int(argv[5])

    if method == "rand":
        rand(dataset, n1, n2)
    elif method == "bfs":
        bfs(dataset, n1, n2, seednum)
    elif method == "dfs":
        bfs(dataset, n1, n2, seednum)
    elif method == "sec":
        bfs(dataset, n1, n2, seednum)
    else:
        sys.exit(1)

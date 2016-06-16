# adjacency_list.py
# py adjacency_list.py <input> <output> <directed>
# エッジリストから隣接リストを生成する

import sys
from collections import defaultdict

argv = sys.argv
input = argv[1]
output = argv[2]
directed = argv[3]

max = 0
al = defaultdict(set)
for line in open(input):
    sp = line.strip().split(" ")
    if directed == "True":
        al[int(sp[0])].add(int(sp[1]))
    elif directed == "False":
        al[int(sp[0])].add(int(sp[1]))
        al[int(sp[1])].add(int(sp[0]))
    else:
        print("format: py adjacencylist.py <input> <output> <directed>")
        sys.exit(0)
    if max < int(sp[0]):
        max = int(sp[0])
    if max < int(sp[1]):
        max = int(sp[1])


with open(output,"w") as f:
    for id in range(1,max+1):
        f.write(str(id))
        if al[id] != None:
            alist = list(al[id])
            for id2 in sorted(alist):
                f.write(" {}".format(id2))
        f.write("\n")

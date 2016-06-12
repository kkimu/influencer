# adjacency_list.py
# エッジリストから隣接リストを生成する

import sys
from collections import defaultdict

argv = sys.argv
input = argv[1]
output = argv[2]

idset = set()
al = defaultdict(list)
for line in open(input):
    sp = line.strip().split(" ")
    al[int(sp[0])].append(int(sp[1]))
    idset.add(int(sp[0]))
    idset.add(int(sp[1]))

print(len(idset))
idlist = list(idset)

with open(output,"w") as f:
    for id in sorted(idlist):
        f.write(str(id))
        if al[id] != None:
            for id2 in sorted(al[id]):
                f.write(" {}".format(id2))
        f.write("\n")

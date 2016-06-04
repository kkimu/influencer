from collections import defaultdict

a = []
cit = defaultdict(lambda : defaultdict(int))

#元データを取得 cit[引用した人][引用された人]=引用回数 を入れる
for line in open("apscitation.csv"):
    sp = line.strip().split(" ")
    cit[sp[0]][sp[1]] += 1

for k1,v1 in cit.items():
    for k2,v2 in v1.items():
        #引用回数が10回以上の場合のみ、情報が拡散したとみなす
        if(v2 >= 10):
            a.append("{} {}\n".format(k1,k2))

a.sort()
f = open("diffusion.txt","w")
for i in a:
    f.write(i)

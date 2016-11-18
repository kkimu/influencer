f = open("link.txt","w")
for line in open("twitternet.csv"):
    sp = line.strip().split(",")
    f.write("{} {}\n".format(sp[0],sp[1]))
f.close

#f = open("link.txt","w")
f = open("diffusion.txt","w")
#for line in open("twitternet.csv"):
for line in open("retweet.csv"):
    sp = line.strip().split(",")
    f.write("{} {}\n".format(sp[1],sp[0]))
f.close

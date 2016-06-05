f = open("link.txt","w")
for line in open("facebook-link.txt"):
    sp = line.strip().split("\t")
    f.write("{} {}\n".format(sp[0],sp[1]))
f.close

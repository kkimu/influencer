f = open("diffusion.txt","w")
for line in open("facebook-wall.txt"):
    sp = line.strip().split("\t")
    f.write("{} {}\n".format(sp[0],sp[1]))
f.close

library(igraph)

t0 <- proc.time()

input <- commandArgs()[5]
directed <- commandArgs()[7]
d <- read.table(input,sep=" ")
if(directed == "True"){
  g <- graph.data.frame(d,directed=T)
}else{
  g <- graph.data.frame(d,directed=F)
}
print("input")
print(proc.time() - t0)

output <- commandArgs()[6]

fn_deg <- paste(output,"deg.list",sep="")
deg <- degree(g,mode="in")
write.table(deg[order(deg,decreasing=T)],fn_deg,quote=F,col.names=F)

print("degree")
print(proc.time() - t0)

fn_pr <- paste(output,"pr.list",sep="")
pr <- page.rank(g)$vector
write.table(pr[order(pr,decreasing=T)],fn_pr,quote=F,col.names=F)

print("PageRank")
print(proc.time() - t0)

fn_kcore <- paste(output,"kcore.list",sep="")
kcore <- graph.coreness(g)
write.table(kcore[order(kcore,decreasing=T)],fn_kcore,quote=F,col.names=F)

print("kcore")
print(proc.time() - t0)

fn_clo <- paste(output,"clo.list",sep="")
clo <- closeness(g, mode="in")
write.table(clo[order(clo,decreasing=T)],fn_clo,quote=F,col.names=F)

print("closeness")
print(proc.time() - t0)

fn_bet <- paste(output,"bet.list",sep="")
bet <- betweenness(g)
write.table(bet[order(bet,decreasing=T)],fn_bet,quote=F,col.names=F)

print("betweenness")
print(proc.time() - t0)


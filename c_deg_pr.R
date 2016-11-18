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
fn_deg <- paste(output,"deg.rank",sep="")
deg <- degree(g,mode="in")
write.table(deg[order(deg,decreasing=T)],fn_deg,quote=F,col.names=F)

print("degree")
print(proc.time() - t0)

fn_pr <- paste(output,"pr.rank",sep="")
pr <- page.rank(g)$vector
write.table(pr[order(pr,decreasing=T)],fn_pr,quote=F,col.names=F)

print("PageRank")
print(proc.time() - t0)

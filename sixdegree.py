import networkx as nx
import numpy
g=nx.read_edgelist("facebook_combined.txt") #txt file not dwnlded
N=list(g.nodes())
spll=[]
for u in N:
    for v in N:
        if u!=v:
            l=nx.shortest_path_length(G,u,v)
            print("shortest psth between ",u," and ",v," is of length ",l)
            spll.append(l)
min_spl=min(spll)
max_spl=max(spll)
avg_spl=numpy.average(spll)
print("minimum shortest length:",min_spl)
print("maximum shortest length:",max_spl)
print("average shortest length:",avg_spl)
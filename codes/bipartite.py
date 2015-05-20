import igraph as ig

__author__ = "hassan abedi"
__email__ = "hassan.abedi.t@gmail.com"

def loadBipartiteGraph(edgelist_file, nodetypes_file, edgelist_sep=" ",
                       directed=False):
    # reading edgelist file 
    edges = []
    with open(edgelist_file, "r") as ef:
        for line in ef:
            edge = line.strip().split(edgelist_sep)
            edges.append((int(edge[0]), int(edge[1])))
            pass
        pass
    # reading the nodes' type file
    nodetypes = []
    with open(nodetypes_file, "r") as ntf:
        for line in ntf:
            nodetypes.append(int(line.strip()))
            pass
        pass
    # constructing a bipartite graph
    return ig.Graph.Bipartite(nodetypes, edges, directed=directed)
    
# testing + debugging

## inside of g.nodetypes (each node has a type, either type 0 or 1)
## 0
## 1
## 1
## 0
## 1

## inside of g.edgelist (each node must connect to the opposite type)
## 0 4
## 0 2
## 0 1
## 1 3
## 2 3
## 3 4

g = loadBipartiteGraph(edgelist_file="../data/bipartite/g.edgelist",
                       nodetypes_file="../data/bipartite/g.nodetypes")


print (g.is_bipartite())



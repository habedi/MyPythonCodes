import networkx as nx
from operator import itemgetter
from collections import OrderedDict

def ppr(g, seed, alpha=0.85, epsilon=10e-8, iters=100):
    pref = {}
    T = [seed]
    for node in g.neighbors(seed):
        T.append(node)
        pass
    for node in g:
        if node in T: 
            pref.update({node:(1.0 / len(T))})
            pass
        else:
            pref.update({node:0.0})
            pass
    pass
    x = nx.pagerank(g, alpha=alpha, personalization=pref, max_iter=iters,
                tol=epsilon)
    return x

def ppr_sorted(g, pprv):
    spprv = {}
    for item in pprv.iteritems():
        k, v = item
        spprv.update({k:(v/g.degree(k))})
        pass
    dspprv = sorted(spprv.items(), key=itemgetter(1), reverse=True)
    return dspprv

def min_cond_cut(g, dspprv, max_cutsize=0):
    
    def conductance(nbunch):
        sigma = 0.0
        vol1 = vol2 = 0
        for node in nbunch:
            for n in g.neighbors(node):
                if n not in nbunch:
                    sigma += 1.0
                    pass
                pass
            pass
        for degseq in g.degree().iteritems():
            node, degree = degseq
            if node not in nbunch:
                vol2 += degree
            else:
                vol1 += degree
            pass
        cond = (sigma / min(vol1, vol2))
        return cond
    
    k = 1
    conductance_list = []

    if max_cutsize < 1:
        limit = (len(dspprv)) # cutsize could be as big as the graph itself
    else:
        limit = max_cutsize # maximum size of the cut with minimum conductance 
        
    while k < limit :
        nbunch = []
        for i in xrange(0, k):
            nbunch.append(dspprv[i][0])
            pass
        #print (k, conductance(nbunch)) # conductane of current cut size
        conductance_list.append((k, conductance(nbunch)))
        k += 1
        pass
    return min(conductance_list, key=itemgetter(1))

## running the code ..
g = loadGraph(gfile='../data/snap-dblp/com-dblp.ungraph.txt')
a = ppr(g, seed=5, alpha=0.85, epsilon=10e-8, iters=100)
b = ppr_sorted(g, pprv=a)
print (min_cond_cut(g, dspprv=b, max_cutsize=10)) # finding the best community around NodeId==5

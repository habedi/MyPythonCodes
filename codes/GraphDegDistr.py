import sys

sys.path.append("../Stanford-SNAP/snap-python/swig")
import snap 

class GraphDegDistr(object):
    def __init__(self, g):
        self.Graph = g
        pass

    def getDegreeDistribution(self, output_file=None):

        if output_file == None:
            for NI in self.Graph.Nodes():
                yield (NI.GetId(), NI.GetOutDeg())
                pass
            return 
        else:
            with open(output_file, "w") as of:
                for NI in self.Graph.Nodes():
                    of.write(str(NI.GetId())+"\t"+str(NI.GetOutDeg())+"\n")
                    pass
        return
        

        
    
        
                

            
    

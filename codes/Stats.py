from __future__ import print_function
import math

# my statistical class
class Stats(object):
    def __init__(self, seq):
        #seq must be a list of real valued numbers
        if isinstance(seq, list):
            self.seq = seq
        else:
            raise Exception
    
    def getCD(self,):
        """ this method process a list of values and return a dictionary containing
            the comulative distribution of each item in the self.seq
            {k=item, v=times seen in the list} """
        freq = {}
        for value in self.seq:
            if value not in freq:
                freq.update({value:1})
            else:
                freq[value] += 1
        return freq

    def getMean(self,):
        return sum(self.seq)/len(self.seq)

    def getMode(self,):
        d = self.getCD()
        return max(d, key=d.get)
    
    def getMedian(self,):
        sseq = sorted(self.seq)
        mid = int(math.floor(len(sseq)%2.0))
        if len(sseq)%2.0 > 0:
            return sseq[mid + 1]
        print ("mid=", mid)
        return (sseq[mid] + sseq[mid + 1])/2.0

# test and debug
s = Stats(seq=[1,1,2,3,45,8,2,0,0.2,-8])
print (s.getCD())
print (s.getMean())
print (s.getMode())
print (s.getMedian())

from __future__ import print_function

import math
import matplotlib.pyplot as plt
import numpy as np

# my statistical class
class Stats(object):
    
    def get_cd(self, seq):
        freq = {}
        for value in seq:
            if value not in freq:
                freq.update({value:1})
            else:
                freq[value] += 1
        return freq

    def get_mean(self, seq):
        return sum(seq)/len(seq)

    def get_mode(self, seq):
        d = self.getCD(seq=seq)
        return max(d, key=d.get)
    
    def get_median(self, seq):
        sseq = sorted(seq)
        mid = int(math.floor(len(sseq)/2.0))
        if len(sseq)%2.0 > 0:
            return sseq[mid]
        return (sseq[mid - 1] + sseq[mid])/2.0

    def heatmap(self, seq_xy, x_labels=[], y_labels=[]):
        xy = np.array(seq_xy)
        if x_labels != [] and x_labels != []:
            fig, ax = plt.subplots()
            heatmap = ax.pcolor(xy, cmap=plt.cm.Reds)
            cbar = plt.colorbar(heatmap)
            ax.set_xticks(np.arange(xy.shape[1]) + 0.5, minor=False)
            ax.set_yticks(np.arange(xy.shape[0]) + 0.5, minor=False)
            ax.invert_yaxis()
            ax.set_xticklabels(x_labels, minor=False)
            ax.set_yticklabels(y_labels, minor=False)
            plt.show()
            return 1
        else:
            plt.pcolor(xy, cmap=plt.cm.Blues)
            plt.colorbar()
            plt.show()
        return 0

# test and debug
seq_x = [1,7,2,3,45,8,3,0,0.2,-8,-5]
seq_xy = np.random.random((4,4))
s = Stats()
print ('[cummulative distribution of data]=>', s.get_cd(seq=seq_x))
print ('[mean of data]=>', s.get_mean(seq=seq_x))
print ('[mode of data]=>', s.get_mode(seq=seq_x))
print ('[median of data]=>', s.get_median(seq=seq_x))
print ('[draw heatmap of data with lables]=>', s.heatmap(seq_xy=seq_xy,
                                           x_labels=['a','b','c','d'],
                                           y_labels=['w','x','y','z']))
print ('[draw heatmap of data with lables]=>', s.heatmap(seq_xy=seq_xy,))

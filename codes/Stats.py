from __future__ import print_function


# my statistical class
class Stats(object):
    def __init__(self,):
        pass
    
    def getCD(self, data_points):
        """ this method takes a list of values and return a dictionary containing
            the comulative distribution of each item in the list
            {k=item, v=times seen in the list} """
        
        if isinstance(data_points, list):
            freq = {}
            for value in data_points:
                if value not in freq:
                    freq.update({value:1})
                else:
                    freq[value] += 1
            return freq
        return None

# test and debug
s = Stats()
print (s.getCD(data_points=[1,1,2,3,45,8,2,0,0.2,-8]))

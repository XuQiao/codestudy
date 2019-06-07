#!/bin/python
import numpy as np
import matplotlib.pyplot as plt
class antpath():
    def __init__(self, n, m):
        self.n = n
        self.m = m
        assert(n > 0 and m > 0)
        self.allpaths = []
        self.Ds = []

    def deviation(self, path):
        D = max([abs(float(p[0])/float(self.n)-float(p[1])/float(self.m)) for p in path])
        return D

    def findallpaths(self, n, m):
        # using dfs
        # length of the path always n + m
        # get all paths of the ant
        if n == 0:
            allpaths = [[(0,y) for y in range(m+1)]] # corner case
        elif m == 0:
            allpaths = [[(x,0) for x in range(n+1)]]
        else:
            direc_x = []
            direc_y = []
            for path in self.findallpaths(n-1, m):
                path.append((n,m))
                direc_x.append(path)
            for path in self.findallpaths(n, m-1):
                path.append((n,m))
                direc_y.append(path)
            #direc_x = [path.append((n,m)) for path in self.findallpaths(n-1, m)]
            #direc_y = [path.append((n,m)) for path in self.findallpaths(n, m-1)]
            allpaths = direc_x + direc_y
        return allpaths

    def findallDs(self, n, m):
        # directly calculate D without calculating paths
        if n == 0:
            Ds = [0] # corner case
        elif m == 0:
            Ds = [0] # corner case
        else:
            Ds = []
            for currD in self.findallDs(n-1, m):
                Ds.append(max(currD, abs(float(n-1)/float(self.n)-float(m)/float(self.m))))
            for currD in self.findallDs(n, m-1):
                Ds.append(max(currD, abs(float(n)/float(self.n)-float(m-1)/float(self.m))))
        return Ds

    def getDs(self, method = 'direct'):
        if method == 'direct':
            self.allpaths = self.findallpaths(self.n, self.m)
            print self.allpaths
            print len(self.allpaths)
            self.Ds = [self.deviation(path) for path in self.allpaths]
        else:
            self.Ds = self.findallDs(self.n, self.m)
        return self.Ds

Ant = antpath(7,11)
Ds = np.asarray(Ant.getDs('direct'))
Ds1 = np.asarray(Ant.getDs('indirect'))
#print (Ds)
print (Ds1)
plt.hist(Ds1)
plt.show()
#print Ds.mean()
print Ds1.mean()
#print Ds.std()
print Ds1.std()
#print float(np.count_nonzero(Ds>0.6)) / float(np.count_nonzero(Ds>0.2))
print float(np.count_nonzero(Ds1>0.6)) / float(np.count_nonzero(Ds1>0.2))

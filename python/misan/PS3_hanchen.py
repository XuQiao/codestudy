import numpy as np
import random
wokp=[0]*1000

def onestep(oldList):
    newList = oldList.copy()
    for i in range(len(oldList)):
        flag = random.random()
        if flag > 0.5:newList[i] = oldList[i] + 1
            else:newList[i] = oldList[i] - 1
    return newList

def gen(shock):
    gen=[100]*len(shock)
    for i in range(len(shock)-1):
        gen[i+1]=gen[i]+shock[i]
    return gen

def annatrans(semidat):
    trans=[0]*(500)
    for i in range(len(trans)):
        trans[i]=semidat[i*2-1]+semidat[i*2]
    return trans

def delta(yeardat):
    change=[0]*(len(yeardat)-1)
    for i in range(len(change)):
        change[i]=yeardat[i+1]-yeardat[i]
    return change

c1=onetep(wokp)
csy=gen(c1)
cy=annatrans(csy)
deltacy=np.array(delta(cy))
y1=onestep(wokp)
ysy=gen(y1)
yy=annatrans(ysy)
deltayy=np.array(delta(yy))
A=np.vstack([deltayy,np.ones(len(deltayy))]).T
m=np.linalg.lstsq(A,deltacy)[0]
m


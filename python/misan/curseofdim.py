import matplotlib.pyplot as plt
import numpy as np

N = 10
def curseofdim(dim, fracs):
#    points = np.random.uniform(0,1.,size=[N]*dim)
    points = []
    for i in range(N*N*dim*dim):
        p=[]
        for _ in range(dim):
            p.append(np.random.uniform(0,1))
        points.append(p)
    dists = [distance(p) for p in points]
    dists = np.sort(dists)
    npoints = len(points)
    rads = []
    for frac in fracs:
        rad = dists[int(frac*npoints)]
        rads.append(rad)
    return rads

def distance(p):
    dis = 0
    for i in p:
        dis += i*i
    return np.sqrt(dis)


def main():
    dims = [1,2,3,4,6,10,20]
    fracs = np.linspace(0.0, 0.99, num=154)
    cs = [curseofdim(dim, fracs) for dim in dims]
    ax = plt.subplot()
    for i in range(len(dims)): 
        line = ax.plot(fracs,cs[i],label='n='+str(dims[i]))
    ax.legend()
    plt.show()

if __name__ == '__main__':
    main()

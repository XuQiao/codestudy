import numpy as np
np.zeros(10)
np.zeros(3,6)
np.zeros((3,6))
np.empty()
np.empty(2)
np.empty((2,3))
np.arrange((2,3))
np.arrnge((2,3))
np.arange((2,3))
np.arange(2)
np.arange(100)
np.array(3)
np.array(3)
np.array(3)a=
a=np.array(3)
a
a[0]
a=[1,2]
b=np.array(a)
b
b[0]
b
a
np.eye(10)
np.identity(10)
assert(np.identity(10)==np.eye(10))
assert(np.identity(10).trace()==np.eye(10).trace())
assert(np.identity(10).trace()==np.eye(10).det())
numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
numeric_strings
numeric_strings.astype(float32)
numeric_strings.astype(float)
a=np.arange(10)
a
a.astype('u4')
a.astype(string)
a.astype(np.string)
a.astype(np.strings)
a.astype(np.string_)
a[1]
a[1]+2
a.astype(np.string_)[1]
a.astype(np.string_)[1]+2
a=np.arange(10,dtype='string_')
arr = np.arange(32).reshape((8, 4))
arr
arr[[1,5,7,2]]
arr[[1,5,7,2]][0,3,1,2]
arr[[1,5,7,2]][[0,3,1,2]]
arr[[1,5,7,2]][:,[0,3,1,2]]
arr[np.ix_([1,5,7,2][0,3,1,2]])
arr[np.ix_([1,5,7,2][0,3,1,2]])]
arr[np.ix_([1,5,7,2][0,3,1,2])]
arr[np.ix_([1,5,7,2],[0,3,1,2])]
arr.T
arr.dot(arr.T)
np.dot(arr.T,arr)
np.dot(arr,arr.T)
arr=randn(7)*5
arr
np.modf(arr)
points = np.arange(-5, 5, 0.01)
xs,ys=np.meshgrid(points,points)
xs
ys
zs=np.meshgrid(points,points)
zs
import matplotlib.pyplot as plt
z=np.sqrt(xs**2+ys**2)
z
plt.imshow(z,cap=plt.cm.gray);plt.colorbar()
plt.imshow(z,cmap=plt.cm.gray);plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
plt.imshow(z,cmap=plt.cm.color);plt.colorbar()
plt.imshow(z);plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
arr=randn(4,4)
arr
np.where(arr>0,2)
np.where(arr>0,2,arr)
np.where(arr>0,2,-2)
np.all()
np.all(axis=1)
arr.all()
arr.any()
arr
arr>0.any()
(arr>0).any()
(arr>0).all()
(arr>0).all(axis=1)
(arr>0).all(axis=2)
(arr>0).all(axis=0)
(arr).all(axis=0)
arr=array([[-0.7139, -1.6331, -0.4959],
[ 0.8236, -1.3132, -0.1935],
[-1.6748, 3.0336, -0.863 ],
[-0.3161, 0.5362, -2.468 ],
[ 0.9058, 1.1184, -1.0516]])
arr
arr.sort()
arr
arr.sort(1)
arr
arr.sort(0)
arr
arr.sort()
arr
arr.sort(1)
arr.sort(0)
arr
X=randn(5,5)
mat=X.T.dot(X)
mat
inv(mat)
mat.dot(inv(mat))
mat.dot(inv(mat))
mat.dot(inv(mat))
q,r=qr(mat)
q
r
diag(mat)
trace(mat)
det(mat)
det(inv(mat))
det(inv(mat))*det(mat))
det(inv(mat))*det(mat)
eig(mat)
svd(mat)
s,v,d=svd(mat)
s
v
d
solve
solve()
solve(mat,X)
lstsq(mat,X)
np.random.normal(size=N)
N=10**7
np.random.normal(size=N)
%timeit np.random.normal(size=N)
from random import normalvariate
%timeit samples=[normalvariate(0,1) for _ in xrange(N)]
np.random.permutation(1000)
np.random.shuffle(1000)
np.random.shuffle(asrange(1000))
np.random.shuffle(arange(1000))
a=np.random.shuffle(arange(1000))
a
a=np.random.shuffle(range(1000))
a
print a
a=np.random.shuffle([1,2,3])
a
np.random.shuffle([1,2,3])
np.shuffle([1,2,3])
np.random.shuffle(xrange(1000))
nstep
nsteps=10000
draws=np.random.randint(0,2,size=nsteps)
steps=np.where(draws>0,1,-1_
)
steps=np.where(draws>0,1,-1)
walk=steps.cumsum()
walk.min()
walk.max()
plt.draw(walk)
plt.plot(walk)
walk.sum()
walk.mean()
walk
walk.std()
np.abs(walk)>10
(np.abs(walk)>10).argmax()
(np.abs(walk)>10)[0]
(np.abs(walk)>10).argmin()
nwalks=5000
draws=np.random.randint(0,2,size=(nwalks,nsteps))
steps=np.where(draws>0,0,-1)
steps=np.where(draws>0,1,-1)
walks=steps.cumsum(1)
walks
walks.sum(1)
walks.mean(1)
walks.mean(1).sum()
walks.max()
walks.min()
hits30 = (np.abs(walks)>-30).any(1)
hits30
hits30 = (np.abs(walks)>300).any(1)
hits30
hits30.sum()
hits30 = (np.abs(walks)>100).any(1)
hits30.sum()
(np.abs(walks)>100)).any(1)
(np.abs(walks)>100).any(1)
(np.abs(walks)>100)).argmax(1)
(np.abs(walks)>100).argmax(1)
(np.abs(walks)>100).argmax(1).mean()
%save
%save numpy
%save numpy.py
%history -f numpy.py

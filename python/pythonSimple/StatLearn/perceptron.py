#Perceptron code
from random import randint

def dotproduct(x, w):
    if(len(x) == len(w)):
        pro = sum([x[i]*w[i] for i in range(len(x))])
        return pro
    else:
        return False

def GramMatrix(x):
    N = len(x)
    G = [[dotproduct(x[i],x[j]) for i in range(N)] for j in range(N)]
    return G

def WrongClassify(x, y, w, b):
    Nwrong = 0
    for i in range(len(x)):
        if y[i]*(dotproduct(x[i],w)+b) <= 0:
            Nwrong += 1
    return Nwrong

def WrongClassifyDualForm(x, y, alpha, b):
    Nwrong = 0
    N = len(x)
    G = GramMatrix(x)
    for i in range(N):
        if y[i]*(sum([alpha[j]*G[j][i]*y[j] for j in range(N)])+b) <= 0:
            Nwrong += 1
    return Nwrong

def OriginPercep(x, y, eta, w, b):
    if(len(x) == len(y)):
        N = len(x)
        while WrongClassify(x, y, w, b) != 0:
            i = randint(0,N-1)
            print (w, b, i, WrongClassify(x, y, w, b))
            if y[i]*(dotproduct(x[i],w)+b) <= 0:
                w = [w[j] + eta*y[i]*x[i][j] for j in range(len(w))]
                b = b + eta*y[i]
        return (w, b)
    else:
        return 0

def DualFormPercep(x, y, eta, alpha, b):
    if(len(x) == len(y)):
        N = len(x)
        G = GramMatrix(x)
        while WrongClassifyDualForm(x, y, alpha, b) != 0:
            i = randint(0,N-1)
            print (alpha, b, i, WrongClassifyDualForm(x, y, alpha, b))
            if y[i]*(sum([alpha[j]*G[j][i]*y[j] for j in range(N)])+b) <= 0:
                alpha[i] = alpha[i] + eta
                b = b + eta*y[i]
        w = [sum([alpha[i]*y[i]*x[i][j] for i in range(N)]) for j in range(len(x[0]))]
        return (alpha, b, w)
    else:
        return 0



x = [[1,3,2],[-1,3,2],[6,3,-1],[2,-0.5,-1]]
#x = [[3,3],[4,3],[1,1]]
y = [-1,1,1,-1]
#y = [1,1,-1]
#w0 = [0,0,0]
w0 = [0,0,0]
b0 = 0
alpha0 = [0,0,0,0]
eta = 1
(w, b) = OriginPercep(x, y, eta, w0, b0)
print (w, b)
G = GramMatrix(x)
print (G)
(alpha, b, w) = DualFormPercep(x, y, eta, alpha0, b0)
print (alpha, b, w)

        

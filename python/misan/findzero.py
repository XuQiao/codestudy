import numpy as np

# Newton's method
# calculate x that makes f(x) = 0
# dx =  - f(x(i)) / df/dx|x(i)
def f(x):
#    if x <= 0:
#        x = -x
    return x*x - 4

def df(x):
    dx = 1e-6
    return (f(x+dx) - f(x)) / dx

def newton(f, x0):
    eps = 1e-6
    x = x0
    while np.fabs(f(x)) > eps:
        dx =  - f(x) / df(x)
        x = x + dx
    return x

def div(f, x1, x2):
    eps = 1e-6
    if x2 < x1:
        x1, x2 = x2, x1
    while f(x1) * f(x2) > 0:
        x1 = 2 * x1 - x2
        x2 = 2 * x2 - x1
    x = (x1 + x2) / 2
    while np.fabs(f((x1+x2)/2)) > eps and f(x1) * f(x2) < 0:
        x = (x1 + x2) / 2
        if f(x) * f(x1) > 0:
            x1 = x
            continue
        if f(x) * f(x2) > 0:
            x2 = x
            continue
    return x

if __name__ == '__main__':
    print "newton: ", newton(f, 3.)
    print "divisive: ", div(f, 1., 10.)

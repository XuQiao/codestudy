import math

def p(n):
    y = math.pow(5,n)/math.factorial(n)/math.exp(5)
    return y

sum = 0

for i in range(20):
#    print p(i)
    sum = sum + p(i)

#print sum

kb = 8.617e-5
T = 2
dE = 5.6e-6
ratio = math.exp(dE/kb/T)
print ratio/(ratio + 1)
print 1/(ratio + 1)

T = dE/kb/math.log(4)
print T

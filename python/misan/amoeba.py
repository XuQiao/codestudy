#There is one amoeba in the pond, each minute the amoeba will either die out, stay the same, split into two, split into three with same probability, what is the probability that the amoeba die out?

#P(E) = sqrt(2) - 1 = 0.414

import random
import numpy
import matplotlib.pyplot as plt
tlimit = 10
dieout = 0
m = 10000
num = []
for world in range(0, m):
    t = 0
    n = 1
    while n > 0 and t < tlimit:
        for i in range(0, n):
            status = random.randint(1, 4)
            if status == 1:
                n = n - 1
            elif status == 3:
                n = n + 1
            elif status == 4:
                n = n + 2
        t = t + 1
    num.append(n)
    if n == 0:
        dieout = dieout + 1

plt.bar(range(0,20), num)
plt.show()
print (dieout * 1./ m)

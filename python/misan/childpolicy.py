# if a village just want boys, every family continues to have children until they have a boy. If they have a girl they continue to give birth, if they have a boy they stop
import random

family = 1000000
b = 0
g = 0
gen = 0;

while (gen < 100):
    for i in range(family):
        baby = bool(random.getrandbits(1)) # 1 : boy, 0 : girl
        if(baby):
            b = b + 1
        else:
            while(not baby):
                g = g + 1
                baby = bool(random.getrandbits(1)) # 1 : boy, 0 : girl
            b = b + 1
    gen  = gen + 1
    print "gen = ", gen
    print "boy = ", b
    print "girl = ", g




        

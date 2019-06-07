# assume person A has money X and person B has money Y. X and Y are integers. Each game 50%/50% they gamble a money(a<X, a<Y), a is an integer too. Until one of them lose all their money. What is the possible that A wins the game finally and what is the possible that B wins the game?
import random

Rounds = 100000
a = 1
i = 0
Awin = 0
Bwin = 0
for Round in range(0, Rounds):
    if Round % 10000 == 0:
        print "has process rounds", Round
    X = 5
    Y = 5
    while True:
        result = bool(random.getrandbits(1))  #assume 1 is A wins and 0 is B wins
        #result = random.choice([True, False])
        if result:
            X = X + a
            Y = Y - a
        else:
            X = X - a
            Y = Y + a
        if X < 0:
            Bwin += 1
            break
        if Y < 0:
            Awin += 1 
            break
    i += 1

print i, Awin, Bwin







        

import random
def calcEx(n):
    arr = range(n)
    random.shuffle(arr)
    counter = 0
    for i in range(len(arr)-1):
        if arr[i+1] == arr[i]+1:
            counter = counter + 1
    return counter

n = 10
E = 0
m = 100000
for i in range(m):
    E = E + calcEx(n) * 1.0 / m
print E
#    print(calcEx(arr))

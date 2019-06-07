listone = [2,3,4]
listtwo = [2*i for i in listone if i>3]
print (listtwo)

def powersum(power, *args):
    '''Return the sum of each arguments raised to specified power'''
    total = 0
    for i in args:
        total = total + pow(i,power)
    return total

print (powersum(1,23,34))
print (powersum(2,10))

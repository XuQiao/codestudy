def fib(n):	#write Fibonacci series up to n
    """Print a Fiboncci series up tp n"""
    a, b=0, 1
    while a < n:
        print a,
        a, b = b, a + b
    print 

fib(2000)

def fib2(n):
    """Return a list containing the FIbonacci series"""
    result=[]
    a,b=0,1
    while a<n:
        result.append(a)
        a,b=b,a+b
    return result[7]

f=fib2(1000)
print f

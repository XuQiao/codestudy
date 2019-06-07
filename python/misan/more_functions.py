def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n','no', 'nop','nope'):
	    return False
        retries = retries - 1
        if retries < 0:
	    raise IOError('refusenik user')
        print complaint

#ask_ok('Do you really want to quit?\n',2)

i = 5
def f(arg=i):
    print arg
i = 6
f()	#will print 5

def f1(a,L=[]):
    L.append(a)
    return L

print f1(1)
print f1(2)

def f2(a,L=None):
    #if L is None:
    L=[]
    L.append(a)
    return L

print f2(1)
print f2(2)

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print "-- This parrot would'n", action,
    print "if you put", voltage, "volts through it."
    print "-- Lovely plumage, the", type
    print "-- It's", state, "!"

parrot(voltage=1000)

print "-" * 40

def cheeseshop(kind, *arguments, **keywords):
    print "-- Do you have any", kind, "?"
    print "-- I'm sorry, we're all out of", kind
    for arg in arguments:
        print arg
    print "-" * 40
    keys = sorted(keywords.keys())
    for kw in keys:
        print kw, ":", keywords[kw]

#It could be called like this:
cheeseshop("Limburger", "It's very runny, sir.",
"It's really very, VERY runny, sir.",
shopkeeper='Michael Palin',
client="John Cleese",
sketch="Cheese Shop Sketch")

args = [3, 6]
print range(*args)

print '-' * 40

def parrot(voltage, state='a stiff', action='voom'):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it.",
    print "E's", state, "!"

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

print '-' * 40

def make_incrementers(n):
    return lambda x: x+n

f = make_incrementers(42)
print f(0)
print f(1)

print '-' * 40

def my_function():
    """Do nothing, but document it.
    
    No really, it doesn't do anything.
    """
    pass

print my_function.__doc__

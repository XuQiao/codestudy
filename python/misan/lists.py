#Basic Lists Functions

print 'list=[1, 2, 3]','\n'

print 'append:'
list=[1, 2, 3]
list.append(3)
print 'list.append(3):',list

list[len(list):]=[4]
print 'list[len(list):]=[4]:',list,'\n'

print 'extend:'
b = [1, 2, 3]
print 'b=',b
c = [4, 5]
print 'c=',c
b.extend(c)
print 'b.extend(c):',b,'\n'

print 'insert:'
list.insert(1,10)
print 'list.insert(1,10):',list,'\n'

print 'remove:'
list.remove(10)
print 'list.remove(10):',list,'\n'

print 'pop:'
list.pop(1)
print 'list.pop(1):',list,'\n'
list.pop()
print 'list.pop():',list,'\n'

print 'find'
a=list[2]
print 'a=list[2]:',a,'\n'

print 'index:'
a1=list.index(3)
print 'a1=list.index(3):',a1,'\n'

print 'count:'
a2=list.count(3)
print 'a2=list.count(3):',a2,'\n'

print 'sort:'
list.sort()
print 'list.sort():',list,'\n'

print 'reverse:'
list.reverse()
print 'list.reverse():',list,'\n'

#Queue

print '-' * 40,'\n'

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry") # Terry arrives
queue.append("Graham") # Graham arrives
print queue.popleft() # The first to arrive now leaves
print queue.popleft() # The second to arrive now leaves
print queue # Remaining queue in order of arrival

#Function Programming Tools

print '-' * 40,'\n'

print 'filter():'
def f(x): 
    return x % 2 != 0 and x % 3 != 0
print filter(f, range(2, 25)),'\n'

print 'map():'
def cube(x):
    return x*x*x
print map(cube,range(0,10)),'\n'

seq = range(8)
def add(x, y): return x+y
print map(add, seq, seq),'\n'

print reduce(add,seq,100)

#print sum(list)

#List Comprehensions
print '-' * 40,'\n'
squares = []
for x in range(10):
    squares.append(x**2)
print squares
#We can obtain the same result with:
squares = [x**2 for x in range(10)]
print squares
squares = map(lambda x: x**2, range(10))
print squares,'\n'

list_comp=[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print list_comp

freshfruit = ['    banana','    loganberry','passion fruit    ']
print [(x, x**2) for x in range(6)]

from math import pi
print [str(round(pi,i)) for i in range(1,6)]

matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print [[row[i] for row in matrix] for i in range(4)]
print zip(*matrix)

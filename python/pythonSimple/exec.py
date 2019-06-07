import sys
print (sys.__name__)
print (repr(sys.__name__))
a=eval(repr('print (sys.__name__)'))
print (a)

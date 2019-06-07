name = 'dafadfa'

if name.startswith('daf'):
    print ('starts with daf')

if 'a' in name:
    print ('a in name')

s = 'afa'
if name.find(s) != -1:
    print ('%s in name, location is %d' %(s,name.find(s)))

delimiter = '_'
mylist = ['a','df','df']
print (delimiter.join(mylist))


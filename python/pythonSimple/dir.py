import mymodule
import sys
import using_name
print (dir(mymodule))
for i in dir(mymodule):
 #   print ('print (mymodule.%s)' %i)
    if '__' in i:
        print ('mymodule. %s = %s' %(i,repr('(mymodule.%s)' %i)))
    else:
        print ('mymodule. %s = %s' %(i,repr('print (mymodule.%s())' %i)))
        
    
#print (dir(sys))
#for i in dir(sys):
    #print ('sys.%s()' %i)
    #print ('sys.' + i + '() = %s' %exec('sys.%s' %i))
#print (dir(using_name))

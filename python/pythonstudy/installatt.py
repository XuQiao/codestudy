class Stu(object):
    def set_age(self,age):
        self.age=age
    age=0
    pass   
print (dir(Stu))
s=Stu()
a=Stu()
from types import MethodType
#s.set_age=MethodType(set_age,s)
#a.set_age=MethodType(set_age,a)
#Stu.set_age=MethodType(set_age,Stu)
a.set_age(15)
print (dir(a))
print (dir(Stu))
s.set_age(11)
print(s.age,a.age)

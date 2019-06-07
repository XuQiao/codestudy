basket =  ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruit = set(basket)
print fruit

print 'apple' in fruit
print 'crabgrass' in fruit

print '-' * 40

list_a = 'abracaabra'
list_b = 'alacazam'
a = set(list_a)
b = set(list_b)

print 'a: ', list_a
print 'b: ', list_b
print 'unique letters in a: ', a
print 'letters in a but not in b: ', a - b
print 'letter in both a and b: ', a | b
print 'letters in a or b but not both: ', a ^ b

#set_c = {'foo', 'foo'}
#print set_c

a = [x for x in 'abracadabrax' if x not in 'abc']
print set(a)


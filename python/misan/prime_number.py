def prime(n0):
	"""find prime numbers small than n0"""
	for n in range(2,n0):
		for x in range(2,n):
			if n%x==0:
				print n,'=',x,'*',n/x
				break
		else:
			print n,'is a prime number'


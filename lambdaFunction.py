def myfunct(n):
	return lambda a: a * n

mydouble = myfunct(7)

print(mydouble(6))

  
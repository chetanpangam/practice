class MyNumbers:
	def __iter__(self):
		self.a = 1
		return self

	def __next__(self):
		if(self.a <= 7):
			x = self.a
			self.a += 1
			return x
		else:
			raise StopIteration

mn = MyNumbers()
myiter = iter(mn)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


"""mytuple = (4, 8 ,6 ,5, 10, 18)
mit = iter(mytuple)

print(next(mit))
print(next(mit))
print(next(mit))
print(next(mit))
print(next(mit))
print(next(mit))


mytuple = ("c", "h","e", "t","a","n")
mit = iter(mytuple)

print(next(mit))
print(next(mit))
print(next(mit))
print(next(mit))
print(next(mit))
print(next(mit))"""

for x in myiter:
	print(x)
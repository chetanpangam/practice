# specialMethods.py

#map()

print("===== map() ========")

def doubler(num):
	if num%2 == 0:
		return num * 2
	else:
		return num


arr = [1,2,3,4,5]
result = map(doubler, arr)
print(result)
print(list(result))


myset = (1,2,3,4)
result1 = set(map(lambda x: x+x, myset))
print(result1)


print("====== divmod() ========")
x= 8
y = 3

a, b = divmod(x, y)
print(a, b)

# Sum of digits of a number using divmod
num = 117
sums = 0
while num != 0:
    use = divmod(num, 10)
    dig = use[1]
    sums = sums + dig
    num = use[0]
print("Sum of digits of {0} is {1}".format(num, sums))


print("====== all() ========")

print(all((91, 22, 33, 44)))
print(all([True, True, False]))

print("====== any() ========")

l = [False, False, True, False, False]
print(any(l))
print(all((0, 0, False, 0)))


print("====== enumerate() ========")

l1 = ["eat", "sleep", "repeat"]
s1 = "geeks"
 
# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)
 
print("Return type:", type(obj1))
print(list(enumerate(l1)))
 
# changing start index to 2 from 0
print(list(enumerate(s1, 2)))


print("====== filter() ========")

# function that filters vowels
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False

# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'o', 'r']
 
# using filter function
filtered = filter(fun, sequence)
 
print('The filtered letters are:')
for s in filtered:
    print(s)

print("====== ord() ========")

print(ord('2'))    
print(ord('g'))    
print(ord('&'))


print("====== reversed() ========")

my_list = ["apple", "banana", "cherry", "date"] 
reversed_list = list(reversed(my_list)) 
print(reversed_list)

my_list1 = ["apple", "banana", "cherry", "date"] 
for val in reversed(my_list):
	print(val)

print("====== zip() ========")

name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]
 
# using zip() to map values
mapped = zip(name, roll_no)

print(type(mapped))
print(mapped)
print(list(mapped))

mapped = zip(name, roll_no)
print(set(mapped))

mapped = zip(name, roll_no)
print(tuple(mapped))

mapped = zip(name, roll_no)
print(dict(mapped))


print("====== textwrap() ========")

import textwrap 
  
value = "asdfasdfasdfasdfasdf"
  
# Wrap this text. 
wrapper = textwrap.TextWrapper(width=4) 
  
word_list = wrapper.wrap(text=value) # returns list of lines

print(word_list)  
# Print each line. 
for element in word_list: 
    print(element) 

value= "qwertyqwertyqwertyqwerty"
str = textwrap.fill(value, width=6) #returns single string with linebreaker
print(str)

print("====== groupby() ========")
from itertools import groupby

seq = "11222344445"
groups = []
uniquekeys = []
for k, g in groupby(seq):
    groups.append(list(g))
    uniquekeys.append(k)

print(groups)
print(uniquekeys)

for key in range(len(groups)):
     print((len(groups[key]), int(uniquekeys[key])), end=" ")
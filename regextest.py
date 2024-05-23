# regextest.py

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt) #Returns a Match object if there is a match anywhere in the string
print(" Match object span", x.span())
print(" Match object group", x.group())
print(" Match object string",x.string)


y = re.findall("ai", txt) #The findall() function returns a list containing all matches.
print("The findall() function", y)

z = re.search("\s", txt)
print("The first white-space character is located in position:", z.start())

a = re.split("\s", txt) # The split() function returns a list where the string has been split at each match
print("The split() function", a)

b = re.sub("\s", "9", txt) # The sub() function replaces the matches with the text of your choice:
print("The sub() function", b)
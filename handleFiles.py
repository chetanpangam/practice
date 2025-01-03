# handleFiles.py

import os

print("=========Create==========")
f = open("python_practice/files/myfile.txt", "x")
print("Created myfile.txt")
f.close()

f = open("python_practice/files/myfile2.txt", "w")
print("Created myfile2.txt")
f.close()


print("=========Write============")
f = open("python_practice/files/myfile.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("python_practice/files/myfile.txt", "r")
print(f.read())


print("======READ==========")
file = open("python_practice/files/myfile.txt", "r")

print(file.read(10))

print(file.read())

print(file.readline())

for x in file:
	print(x)

file.close()


print("======Append==========")

file2 = open("python_practice/files/myfile2.txt", "a")
file2.write("Appending content to existing file!")

file2.close()

file3 = open("python_practice/files/myfile2.txt")
print(file3.read())


print("========Delete/Remove========")

os.remove("python_practice/files/myfile.txt")
print("Removed myfile.txt")

if os.path.exists("python_practice/files/myfile2.txt"):
	os.remove("python_practice/files/myfile2.txt")
	print("Removed myfile2.txt")
else:
	print("File does not exists")
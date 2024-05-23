# handleFiles.py

import os

print("======READ==========")
file = open("demofile.txt", "r")

# print(file.read(10))

# print(file.read())

# print(file.readline())

for x in file:
	print(x)

file.close()


print("======Append==========")

file2 = open("demofile2.txt", "a")
file2.write("Appending content to existing file!")

file2.close()

file3 = open("demofile2.txt")
print(file3.read())


print("=========Write============")
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())


print("=========Create==========")
f = open("myfile.txt", "x")
print("Created myfile.txt")
f.close()

f = open("myfile2.txt", "w")
print("Created myfile2.txt")
f.close()

print("========Delete/Remove========")

os.remove("myfile.txt")
print("Removed myfile.txt")

if os.path.exists("myfile2.txt"):
	os.remove("myfile2.txt")
	print("Removed myfile2.txt")
else:
	print("File does not exists")
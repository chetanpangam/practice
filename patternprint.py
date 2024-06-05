# patternprint.py

input_value = input()
n, m = input_value.split(" ")
n, m = int(n), int(m)
pattern = ".|."
val = "WELCOME"



for i in range(n//2):
    print((pattern*i).rjust(m//2 - 1 , '-')+pattern+(pattern*i).ljust(m//2 - 1,'-'))
     
print(val.center(m,'-'))

for i in range(n//2 , 0 , -1):
    print((pattern*(i-1)).rjust(m//2 - 1, '-')+pattern+(pattern*(i-1)).ljust(m//2 -1, '-'))
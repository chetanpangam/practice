# swap.py
# Swap two numbers

x=4
y=5

print(f"original x = {x} and y = {y}")

x, y = y, x

print(f"Swapping varibles on same line: x = {x} and y = {y}")

temp = x
x = y
y = temp

print(f"Swapping using temp varible: x = {x} and y = {y}")


x = x ^ y
y = x ^ y
x = x ^ y

print(f"Swapping using XOR: x = {x} and y = {y}")
def set(num, pos):
    # First step = Shift '1'
    # Second step = Bitwise OR
    num |= (1 << pos)
    print(num)


num, pos = 4, 1

set(num, pos)


def unset(num, pos):
    # Second Step: Bitwise AND this number with the given number
    num &= (~(1 << pos))
    print(num)


num, pos = 7, 1

unset(num, pos)


def at_position(num, pos):
    bit = num & (1 << pos)
    return bit


num = 7
pos = 2
bit = at_position(num, pos)
print(bit)

print("==============")

def isPowerOfTwo(x):
    # First x in the below expression is
    # for the case when x is 0
    return x and (not(x & (x - 1)))

print(isPowerOfTwo(8))
print(isPowerOfTwo(7))
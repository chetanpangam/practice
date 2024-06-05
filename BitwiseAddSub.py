def getSum(a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """
    bitShort = 0xffffffff
    while(b & bitShort != 0):
        print(b)
        print(bitShort)
        c = a&b
        a = a^b
        b = c<<1
    return a & bitShort if b > 0 else a

def getSub(a,b):
    while(b != 0):
        carry = ((~a) & b) << 1
        a = a ^ b
        b = carry
    return a



print(getSum(4,10))
# print(getSub(-2,4))
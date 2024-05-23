import math
def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 0:
        return 0

    limit = math.floor(math.log2(n))
    count = 0

    for i in range(0, limit + 1):
        ans = n & (1 << i)
        if ans:
            count += 1
    
    return count



n = 11
res = hammingWeight(n)
print(res)
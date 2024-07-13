'''
Using temp1.py and temp2.py to understand the importance of the if __name__ == '__main__': statement.
'''

from temp1 import add

def addWithSquare(n):
    square = n * n
    result = add(n, square)
    return result

n = int(input())
print(__name__)
print("Add with Square: ", addWithSquare(n))
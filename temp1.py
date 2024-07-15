'''
Using temp1.py and temp2.py to understand the importance of the if __name__ == '__main__': statement.
'''

def add(x, y):
    return x + y

if __name__ == '__main__':
    x= int(input())
    y = int(input())
    print(__name__)
    print("Addition: ", add(x, y))
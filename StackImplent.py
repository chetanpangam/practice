# StackImplent.py

class StackImplent:

    def __init__(self, max):
        self.top = 0
        self.stack = [None]* max
        self.max = max

    def isEmpty(self):
        return self.top == 0

    def isFull(self):
        return self.top == self.max

    def peek(self):
        return self.stack[self.top]
    
    def pop(self):
        if self.isEmpty():
            return -1
        
        
        self.top -= 1
        val = self.stack[self.top] 
        return val
    
    def push(self, val):
        if self.isFull():
            return "Already full"
        self.stack[self.top] = val
        self.top += 1
        return "Successful Insertion"


# Driver Code
if __name__=='__main__':

    st = StackImplent(10)

    print(st.push(11))
    print(st.push(22))
    print(st.isEmpty())
    print(st.pop())
    print(st.pop())
    print(st.isEmpty())
    print(st.push(23))
    print(st.push(33))
    print(st.push(44))
    print(st.isFull())
    print(st.isEmpty())
    print(st.push(23))
    print(st.push(33))
    print(st.push(44))
    print(st.push(23))
    print(st.push(33))
    print(st.push(44))
    print(st.push(23))
    print(st.push(33))
    print(st.push(44))

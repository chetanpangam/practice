# Enter your code here. Read input from STDIN. Print output to STDOUTzz
class Solution:
    def __init__(self):
        self.string = ""
        self.stack = []
        
    def add(self, val, isundo=False):
        self.string += val
        if not isundo:
            self.stack.append([2, len(val)])
            print(self.stack)
        print(self.string)

    def delete(self, val, isundo=False):
        if not isundo:
            self.stack.append([1, self.string[-val:]])
            print(self.stack)
        del_val = self.string[:len(self.string)-val]
        self.string=del_val
        
        print(self.string)

    def undo(self):
        op, val = self.stack.pop()
        if op == 1:
            self.add(val, True)
        elif op == 2:
            self.delete(val, True)
        print(self.string)
    
    def print_val(self, val):
        print(self.string[val - 1])
        print(self.string)

Q=int(input())
solution = Solution()

for _ in range(Q):
    inputs = input().split()
    if len(inputs) > 1:
        op, val = inputs
    else:
        op = inputs[0]
    
    op = int(op)
    if op == 1:
        solution.add(val=val)
    elif op == 2:
        solution.delete(val=int(val))
    elif op == 4:
        solution.undo()
    else:
        solution.print_val(int(val))

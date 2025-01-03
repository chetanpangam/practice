#LinkedListStack.py
'''
Implementing the Stack using the LinkedList. Operation performed push(val), pop(), peek(), isEmpty()
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

class Stack:
    def __init__(self):
        self.stack = LinkedList()
    
    def isEmpty(self):
        if self.stack.head is None:
            return True
        else:
            return False
    
    def push(self, val):
        node = Node(val)
        if self.stack.head is None:
            self.stack.head = node
        else:
            node.next = self.stack.head
            self.stack.head = node
            
    def pop(self):
        if not self.isEmpty():
            result = self.stack.head
            self.stack.head = self.stack.head.next
            return result.data
        else:
            return "Stack is empty"

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.head.data
    
    def __repr__(self) -> str:
        if not self.isEmpty():
            node = self.stack.head
            nodes = []
            while node is not None:
                nodes.append(node.data)
                node = node.next
            nodes.append("None")
            return " -> ".join(nodes)
        else:
            return "Stack is empty"

if __name__ == "__main__":
    stack = Stack()

    stack.push("d")
    stack.push("i")
    stack.push("c")
    stack.push("e")
    print(stack.peek())
    print(stack.__repr__())
    print(stack.pop())
    print(stack.__repr__())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    stack.push("c")
    print(stack.__repr__())
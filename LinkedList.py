class Node:
    def __init__(self, val):
        self.Next = None
        self.val = val

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.Next is not None:
                curr = curr.Next
            
            curr.Next = new_node

    def display(self):
        curr = self.head
        while curr is not None:
            print(curr.val, end=" ")
            curr = curr.Next
        print()

    def search(self, key):
        curr = self.head
        while curr is not None:
            if curr.val == key:
                print(f"Found key {key} in the LL")
                return
            curr = curr.Next
        print(f"The key {key} is not present in the LL")

    def reverse(self):
        prev = None
        curr = self.head

        while curr is not None:
            nxt = curr.Next
            curr.Next = prev
            prev = curr
            curr = nxt
        self.head = prev
    
    def delete(self, pos):
        prev= None
        curr = self.head
        index= 0
        if curr is None:
           return
        while curr.Next is not None and index<pos:
            prev = curr
            curr = curr.Next
            index += 1
        if index < pos:
            print("Index out of range")
        elif index == 0:
            self.head = self.head.Next
        else:
            prev.Next = curr.Next
            curr = None




if __name__=="__main__":
    l = LinkedList()
    l.push(4)
    l.push(8)
    l.push(6)
    l.push(2)
    l.display()
    l.push(0)
    l.push(10)
    l.display()
    l.reverse()
    l.display()
    l.search(6)
    l.search(4)
    l.search(24)
    l.delete(1)
    l.display()
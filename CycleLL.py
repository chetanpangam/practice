# Detect loop/cycle in the Linked list
class Node: 
  
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
  
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    # Function to insert a new node at the beginning 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    # Utility function to print it the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data)
            temp = temp.next
  
    def detectLoop(self): 
        if not self.head or not self.head.next:
            return False
        
        stack = []

        while self.head:
            print(id(self.head))
            if id(self.head) in stack:
                return True
            stack.append(id(self.head))
            self.head = self.head.next

        return False
  
  
# Driver program for testing 
llist = LinkedList() 
llist.push(20) 
llist.push(4) 
llist.push(15) 
llist.push(10) 
  
# Create a loop for testing 
llist.head.next.next.next.next = llist.head 
if(llist.detectLoop()): 
    print("Found Loop")
else: 
    print("No Loop")
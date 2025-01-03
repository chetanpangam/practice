# LinkedListQueue.py

class LinkedList:
    def __init__(self):
        self.head = None

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Queue:
    def __init__(self):
        self.queue = LinkedList()
    
    def isEmpty(self):
        if self.queue.head is None:
            return True
        else:
            return False
    
    def enqueue(self, val):
        node = Node(val)

        if self.isEmpty():
            self.queue.head = node
        else:
            node.next = self.queue.head
            self.queue.head.prev = node
            self.queue.head = node
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        elif self.queue.head.next is None:
            result = self.queue.head.data
            self.queue.head = None
            return result
        else:

            prev = self.queue.head

            while prev.next.next is not None:
                prev = prev.next

            result = prev.next.data
            prev.next = None
            
            
            return result
    
    def display(self) -> str:
        if not self.isEmpty():
            node = self.queue.head
            nodes = []
            while node is not None:
                nodes.append(node.data)
                node = node.next
            nodes.append("None")
            return " -> ".join(nodes)
        else:
            return "Queue is empty"

if __name__ == "__main__":
    queue = Queue()

    queue.enqueue("N")
    queue.enqueue("A")
    queue.enqueue("T")
    queue.enqueue("E")
    queue.enqueue("H")
    queue.enqueue("C")
    print(queue.display())
    print(queue.dequeue())
    print(queue.display())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.display())
    queue.enqueue("N")
    print(queue.display())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
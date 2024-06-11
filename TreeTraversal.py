
class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
def inOrder(root):
    if root is None:
        return
    
    curr = root
    stack = []

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        
        curr = stack.pop()
        print(curr.info, end=" ")
        curr = curr.right

def preOrder(root):

    if root is None:
        return

    stack = []
    stack.append(root)

    while len(stack) > 0:
        node = stack.pop()
        print(node.info, end=" ")
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def levelOrder(root):
    if root is None:
        return
    
    queue = []
    queue.append(root)

    while queue:
        node = queue.pop(0)
        print(node.info, end=" ")

        if node.left:
            queue.append(node.left)
        
        if node.right:
            queue.append(node.right)

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print("\nInOrder")
inOrder(tree.root)
print("\n")
print("PreOrder")
preOrder(tree.root)
print("\n")
print("LevelOrder")
levelOrder(tree.root)
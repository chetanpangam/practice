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


def left_view(root):
    if not root:
        return []
    level_map = {}
    from collections import deque
    q = deque([(root, 0)])
    while q:
        node, level = q.popleft()
        if level not in level_map:
            level_map[level] = node.info
        if node.left:
            q.append((node.left, level+1))
        if node.right:
            q.append((node.right, level+1))
    print(level_map)
    n = max(level_map)
    return [level_map[level] for level in range(n+1)]


def right_view(root):
    if not root:
        return []
    level_map = {}
    from collections import deque
    q = deque([(root, 0)])
    while q:
        node, level = q.popleft()
        level_map[level] = node.info
        print(level_map)
        if node.left:
            q.append((node.left, level+1))
        if node.right:
            q.append((node.right, level+1))
    print(level_map)
    n = max(level_map)
    return [level_map[level] for level in range(n+1)]


from collections import deque
def top_view(root):
    if not root:
        return []
    pos_map = {}
    q = deque([(root, 0)])
    while q:
        node, pos = q.popleft()
        if pos not in pos_map:
            pos_map[pos] = node.info
        if node.left:
            q.append((node.left, pos-1))
        if node.right:
            q.append((node.right, pos+1))
    print(pos_map)    
    m, n = min(pos_map), max(pos_map)
    
    return [pos_map[pos] for pos in range(m, n+1)]

from collections import deque
def bottom_view(root):
    if not root:
        return []
    pos_map = {}
    q = deque([(root, 0)])
    while q:
        node, pos = q.popleft()
        pos_map[pos] = node.info
        if node.left:
            q.append((node.left, pos-1))
        if node.right:
            q.append((node.right, pos+1))
    print(pos_map)    
    m, n = min(pos_map), max(pos_map)
    
    return [pos_map[pos] for pos in range(m, n+1)]

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print("\nLeft View")
print(left_view(tree.root))

print("\nRight View")
print(right_view(tree.root))

print("\nTop View")
print(top_view(tree.root))

print("\nBottom View")
print(bottom_view(tree.root))
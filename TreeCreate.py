class Node:
    def __init__(self, val, info):
        self.val = val
        self.info = info
        self.left = None
        self.right = None

# Define a function to perform an inorder traversal of a binary tree
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(f"{node.val} - {node.info}", end=' ')
        inorder(node.right)

# Define a function to create a binary tree from an array of parent nodes
def create_tree(parent, info):
    n = len(parent)
    # Initialize an empty dictionary to keep track of nodes created so far
    nodes = {}
    root = None
    for i in range(n):
        # If the current node is the root node, create it
        if parent[i] == -1:
            root = Node(i, info[i])
            nodes[i] = root
        else:
            # If the parent node exists, get it from the dictionary
            parent_node = nodes.get(parent[i], None)
            # If the parent node does not exist yet, create it
            if parent_node is None:
                parent_node = Node(parent[i], info[i])
                nodes[parent[i]] = parent_node
            # Create a new node and link it to its parent node
            current_node = Node(i, info[i])
            if parent_node.left is None:
                parent_node.left = current_node
            else:
                parent_node.right = current_node
            # Add the new node to the dictionary
            nodes[i] = current_node
    # Return the root node of the constructed tree
    return root

# Example usage:
parent = [-1, 0, 1, 2, 0]
info = [5, 7, -10, 4, 15]
root = create_tree(parent, info)

print(inorder(root))
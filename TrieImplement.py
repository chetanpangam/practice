class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.word_end = False

def insert(root, word):
    curr = root

    for char in word:
        idx = ord(char) - ord('a')

        if not curr.child[idx]:
            curr.child[idx] = TrieNode()
        
        curr = curr.child[idx]
    
    curr.word_end = True


def search(root, word):
    
    curr = root

    for char in word:
        idx = ord(char) - ord('a')

        if not curr.child[idx]:
            return False
        
        curr = curr.child[idx]
    
    return curr.word_end and curr

def search_prefix(root, prefix):
    curr = root

    for char in prefix:
        idx = ord(char) - ord('a')
        if not curr.child[idx]:
            return False
        curr = curr.child[idx]
    
    return True

root = TrieNode()
names = ["and", "ant", "do", "geek", "dad", "ball"]
for name in names:
    insert(root, name)

search_keys = ["do", "gee", "bat"]
for s in search_keys:
    print(f"Key : {s}")
    if search(root, s):
        print("Word Present")
    elif search_prefix(root, s):
        print("Prefix Present")
    else:
        print("Not Present")
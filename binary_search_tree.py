class BSTNode:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def insert(node, key):
    if node is None: return BSTNode(key)
    if key < node.val:
        node.left = insert(node.left,key)
    else:
        node.right = insert(node.right,key)
    return node

def print_sorted(root):
    def dfs(node):
        if not node: return []
        left = dfs(node.left)
        right = dfs(node.right)
        return left + [node.val] + right
    res = dfs(root)
    print(res)
    return res

def predecessor(node):
    node = node.left
    while node.right: node = node.right
    return node.val

def successor(node):
    node = node.right
    while node.left: node = node.left
    return node.val

def deleteNode(node, key):
    if not node: return None

    if key > node.val:
        node.right = deleteNode(node.right, key)
    elif key < node.val:
        node.left = deleteNode(node.left, key)
    else:
        if not (node.left or node.right):
            node = None
        elif node.right:
            node.val = successor(node)
            node.right = deleteNode(node.right, node.val)
        else:
            node.val = predecessor(node)
            node.left = deleteNode(node.left, node.val)
    return node


root = BSTNode(1)
insert(root,2)
insert(root,3)
insert(root,4)
insert(root,5)
insert(root,6)
print_sorted(root)
deleteNode(root,2)
deleteNode(root,3)
deleteNode(root,4)
deleteNode(root,5)
deleteNode(root,6)
print_sorted(root)

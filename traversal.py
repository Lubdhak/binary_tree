from info import *

def inorder_traversal_recursive(root):
	if root == None: return []
	left_tree = inorder_traversal_recursive(root.left)
	right_tree = inorder_traversal_recursive(root.right)
	return left_tree + [root.data] + right_tree

def preorder_traversal_recursive(root):
	if root == None: return []
	left_tree = preorder_traversal_recursive(root.left)
	right_tree = preorder_traversal_recursive(root.right)
	return [root.data] + left_tree + right_tree

def postorder_traversal_recursive(root):
	if root == None: return []
	left_tree = postorder_traversal_recursive(root.left)
	right_tree = postorder_traversal_recursive(root.right)
	return left_tree + right_tree + [root.data]

def inorder_traversal_iterative(root):
	if root is None: return
	stack = [];results=[]
	while True:
		if root is not None:
			stack.append(root)
			root = root.left
		elif stack:
			root = stack.pop()
			results.append(root.data)
			root = root.right
		else:
			break
	return results

def preorder_traversal_iterative(root):
	if root is None: return
	stack = [root]; results=[]
	while stack:
		node = stack.pop()
		results.append(node.data)
		if node.right: stack.append(node.right)
		if node.left: stack.append(node.left)
	return results

def postorder_traversal_iterative(root):
	if root is None: return
	stack = [root]; results=[]
	while stack:
		node = stack.pop()
		results.append(node.data)
		if node.left: stack.append(node.left)
		if node.right: stack.append(node.right)
	return results[::-1]

def levelorder_traversal_iterative(root):
	if root is None: return
	queue = [root]; results=[]
	while queue:
		node = queue.pop(0)
		results.append(node.data)
		if node.left: queue.append(node.left)
		if node.right: queue.append(node.right)
	return results

def levelorder_traversal_recursive(root):
	if root is None: return []
	height = get_tree_height(root)
	return [_get_current_level(root, i, []) for i in range(height)]

def _get_current_level(root, level, results):
	if root==None: return []
	if level==0: results.append(root.data)
	_get_current_level(root.left, level-1, results)
	_get_current_level(root.right, level-1, results)
	return results
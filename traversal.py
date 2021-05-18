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
	result = {}
	for horizontal_level in range(height):
		result[horizontal_level] = __get_current_horizontal(root, horizontal_level, [])
	return result

def __get_current_horizontal(root, current_horizontal_idx, results):
	if root==None: return []
	if current_horizontal_idx == 0: results.append(root.data)
	__get_current_horizontal(root.left, current_horizontal_idx - 1, results)
	__get_current_horizontal(root.right, current_horizontal_idx - 1, results)
	return results

def vertical_order_traversal_recursive(root):
	if root is None: return []
	minimum, maximum = find_min_max_vertical_idx(root)
	result = {}
	for vertical_level in range(minimum, maximum+1):
		result[vertical_level] = __get_current_vertical(root, vertical_level, 0, [])
	return result

def __get_current_vertical(node, vertical_idx, current_vertical_idx, results):
	if node is None: return []
	if current_vertical_idx == vertical_idx: results.append(node.data)
	__get_current_vertical(node.left, vertical_idx, current_vertical_idx - 1 , results)
	__get_current_vertical(node.right, vertical_idx, current_vertical_idx + 1 , results)
	return results


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
	if root is None: return
	root_idx = 0 ; result_map = {}
	__vertical_order_traversal_recursive(root, root_idx, result_map)
	return sorted(result_map.items())

def __vertical_order_traversal_recursive(node, vertical_idx, result_map):
	if node is None: return
	if vertical_idx in result_map:
		result_map[vertical_idx].append(node.data)
	else:
		result_map[vertical_idx] = [node.data]
	__vertical_order_traversal_recursive(node.left, vertical_idx - 1, result_map)
	__vertical_order_traversal_recursive(node.right, vertical_idx + 1, result_map)
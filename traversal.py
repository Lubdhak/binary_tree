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

def levelorder_items_recursive(root):
	if root is None: return
	result_map = {} ; root_idx = 0
	__levelorder_items_recursive(root, root_idx, result_map)
	return (sorted(result_map.items()))

def __levelorder_items_recursive(node, horizontal_idx, result_map):
	if node is None: return 0
	if horizontal_idx in result_map:
		result_map[horizontal_idx].append(node.data)
	else:
		result_map[horizontal_idx] = [node.data]
	__levelorder_items_recursive(node.left, horizontal_idx + 1, result_map)
	__levelorder_items_recursive(node.right, horizontal_idx + 1, result_map)

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

def inorder_without_extra_space(root):
	current = root
	while current is not None:
		if current.left is None:
			yield current.data
			current = current.right
		else:
			pre = current.left
			while pre.right is not None and pre.right is not current:
				pre = pre.right
			if pre.right is None:
				pre.right = current
				current = current.left
			else:
				pre.right = None
				yield current.data
				current = current.right
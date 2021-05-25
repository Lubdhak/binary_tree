from node import *

def insert(root,data):
	queue = [root]
	while len(queue):
		curr_root = queue.pop(0)
		if curr_root.left == None:
			curr_root.left = Node(data)
			break
		else:
			queue.append(curr_root.left)

		if curr_root.right == None:
			curr_root.right = Node(data)
			break
		else:
			queue.append(curr_root.right)

def delete(root, data):
  queue = [root]; last_child = None ; target_node = None
  while queue:
    node = queue.pop(0)
    if node.data == data: target_node = node
    if node.left == node.right == last_child == None:
      last_child = node
    if node.left: queue.append(node.left)
    if node.right: queue.append(node.right)
    if last_child and target_node: break
  if not target_node: return
  target_node.data = last_child.data
  last_child.data = None
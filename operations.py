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
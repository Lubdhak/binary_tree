class Node:
	def __init__(self,data):
		self.left = None
		self.data = data
		self.right = None

def sample_tree():
	#		 [18]
# 	    / 	 \
# 	[211] 	  [20]
# 	/  \ 	  /  \
# [23] [89] [10] [32]
	root = Node(18)
	root.left = Node(211)
	root.right = Node(20)
	root.right.right = Node(32)
	root.right.left = Node(10)
	root.left.right = Node(89)
	root.left.left = Node(23)
	return root

from traversal import *
from node import *
from operations import *
from info import *

my_tree = sample_tree()


# print(get_tree_height(my_tree))

# print(inorder_traversal_recursive(my_tree))
print(levelorder_traversal_recursive(my_tree))

# 23
# 221
# 18,89,10
# 20
# 32

# -------------------------

# def vertical_tree(root):
# 	dic = {}

# 	DFS()


# result_dict = {
# 	0: [],
# 	1: [],
# 	2: [],
# }

# def DFS(node, row, column, result_dict):
# 	if node == None: return
# 	if column not in result_dict:
# 		result_dict[column] = 


# def verticalTraversal(self, root: TreeNode):
#         dic=defaultdict()
#         def DFS(node,r,c):
#             if not node:
#                 return
#             if c not in dic:
#                 dic[c]=defaultdict(list)
#                 dic[c][r].append(node.val)
#             else:
#                 dic[c][r].append(node.val)
#             DFS(node.left,r+1,c-1)
#             DFS(node.right,r+1,c+1)
#         DFS(root,0,0)
#         ans=[]
#         for _,v in sorted(dic.items(),key=lambda item:item[0]):
#             tmp=[]
#             for _,v2 in sorted(v.items(),key=lambda item:item[0]):#v is dictionary
#                 v2.sort()
#                 tmp.extend(v2)
#             ans.append(tmp)
#         return ans
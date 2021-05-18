from traversal import *
from node import *
from operations import *
from info import *

my_tree = sample_tree()

print(inorder_traversal_recursive(my_tree))
print(inorder_traversal_iterative(my_tree))

print(preorder_traversal_recursive(my_tree))
print(preorder_traversal_iterative(my_tree))

print(postorder_traversal_recursive(my_tree))
print(postorder_traversal_iterative(my_tree))

print(levelorder_traversal_iterative(my_tree))
print(levelorder_traversal_recursive(my_tree))

print(get_tree_height(my_tree))


# 23
# 221
# 18,89,10
# 20
# 32
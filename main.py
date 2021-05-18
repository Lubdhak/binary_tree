from traversal import *
from node import *

my_tree = sample_tree()

print(inorder_traversal_recursive(my_tree))
print(inorder_traversal_iterative(my_tree))

print(preorder_traversal_recursive(my_tree))
print(preorder_traversal_iterative(my_tree))

print(postorder_traversal_recursive(my_tree))
print(postorder_traversal_iterative(my_tree))

print(levelorder_traversal_iterative(my_tree))
print(levelorder_traversal_recursive(my_tree))

print(vertical_order_traversal_recursive(my_tree))
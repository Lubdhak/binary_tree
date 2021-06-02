from traversal import *
from node import *

my_tree = sample_tree()

print(inorder_traversal_recursive(my_tree))
print(inorder_traversal_iterative(my_tree))
for v in inorder_without_extra_space(my_tree):
    print(v, end=' ')

print(preorder_traversal_recursive(my_tree))
print(preorder_traversal_iterative(my_tree))

print(postorder_traversal_recursive(my_tree))
print(postorder_traversal_iterative(my_tree))

print(levelorder_traversal_iterative(my_tree))
print(levelorder_items_recursive(my_tree))

print(vertical_order_traversal_recursive(my_tree))




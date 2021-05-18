from info import get_tree_height
from node import *

my_tree = sample_tree

def tree_height(root):
  if root is None: return 0
  l_h = tree_height(root.left)
  r_h = tree_height(root.right)
  return max(l_h,r_h)+1

def vertical_order(root):
  if root is None: return
  height = tree_height(root)
  for i in range(height+1):
    





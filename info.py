def get_tree_height(root):
  if root is None: return 0
  l_height = get_tree_height(root.left)
  r_height = get_tree_height(root.right)
  return max(l_height, r_height) + 1
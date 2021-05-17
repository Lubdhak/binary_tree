def get_tree_width(root):
  left_count = 0 ; right_count = 0
  current = root
  while current.left:
    left_count += 1
    current = current.left
  current = root
  while current.right:
    right_count += 1
    current = current.right
  return left_count + right_count + 1

def get_tree_height(root):
  if root is None: return 0
  l_height = get_tree_height(root.left)
  r_height = get_tree_height(root.right)
  return max(l_height, r_height) + 1
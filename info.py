def unused_get_tree_height(root):
  if root is None: return 0
  l_height = get_tree_height(root.left)
  r_height = get_tree_height(root.right)
  return max(l_height, r_height) + 1

def unused_find_min_max_vertical_idx(root):
  if root is None: return
  minimum = [0] ; maximum = [0] ; root_idx = 0
  __find_min_max_vertical_idx(root, minimum, maximum, root_idx)
  return (minimum[0],maximum[0])

def unused___find_min_max_vertical_idx(node, minimum, maximum, vertical_idx):
  if node is None: return
  minimum[0] = min(minimum[0], vertical_idx)
  maximum[0] = max(maximum[0], vertical_idx)
  __find_min_max_vertical_idx(node.right, minimum, maximum, vertical_idx+1)
  __find_min_max_vertical_idx(node.left, minimum, maximum, vertical_idx-1)

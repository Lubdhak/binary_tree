def get_cousins_of(root, target_node_data):
	if root is None: return
	target_level_idx = None
	queue =[[root,0,None]]
	c_parent = None
	visited_nodes={}
	while queue:
		node, current_level, parent = queue.pop(0)
		if current_level in visited_nodes:
			visited_nodes[current_level].append([node.data, parent])
		else:
			visited_nodes[current_level] = [[node.data, parent]]
		if target_level_idx and current_level > target_level_idx: break
		if node.data == target_node_data:
			target_level_idx = current_level
			c_parent = parent
		if node.left: queue.append([node.left, current_level+1, node])
		if node.right: queue.append([node.right, current_level+1, node])
	if not target_level_idx: return []
	result = []
	for data, parent in visited_nodes[target_level_idx]:
		if c_parent != parent: result.append(data)
	return result

def get_postorder(inorder, preorder):
  inorder_end_idx = len(preorder) - 1
  inorder_start_idx = 0
  global current_preorder_idx ; current_preorder_idx = 0
  global invalue_inidx_map ; invalue_inidx_map = { k: v for v, k in enumerate(inorder)}
  return __get_postorder(inorder, preorder, inorder_start_idx, inorder_end_idx)

def __get_postorder(inorder, preorder, inorder_start_idx, inorder_end_idx):
  global current_preorder_idx
  if inorder_start_idx > inorder_end_idx: return []
  inorder_root_idx = invalue_inidx_map[preorder[current_preorder_idx]]
  current_preorder_idx += 1
  left_tree = __get_postorder(inorder, preorder, inorder_start_idx, inorder_root_idx - 1)
  right_tree = __get_postorder(inorder, preorder, inorder_root_idx + 1, inorder_end_idx)
  return left_tree + right_tree + [inorder[inorder_root_idx]]
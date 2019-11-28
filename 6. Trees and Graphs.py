# DEPTH FIRST SEARCH
def is_balanced(tree_root):

    # Determine if the tree is superbalanced
    
    if tree_root is None:
        return True
        
    depths = []
    
    nodes = []
    nodes.append((tree_root, 0))
    
    while len(nodes):
        node, depth = nodes.pop()
        
        if (not node.left) and (not node.right):
            if depth not in depths:
                depths.append(depth)
                
                if (len(depths) > 2) or (len(depths) == 2 and abs(depths[0] - depths[1] > 1)):
                    return False
        
        else:
            if node.left:
                nodes.append((node.left, depth + 1))
            if node.right:
                nodes.append((node.right, depth + 1))

    return True

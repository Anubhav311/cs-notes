# DEPTH FIRST SEARCH
# O(n) time and O(n)O(n) space
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

# PATTERN LEARNED
'''
For this problem, DFS makes more sense because we don't have to traverse the whole tree. If we find the solution in between somewhere, we can just stop and return False. DFS reaches leaves faster than BFS.

DFS uses a stack. BFS uses a queue.
That's not just a clue about implementation, it also helps with figuring out the differences in behavior. Those differences come from whether we visit nodes in the order we see them (first in, first out) or we visit the last-seen node first (last in, first out).
'''
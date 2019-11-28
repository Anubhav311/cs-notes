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



# BINARY SEARCH TREE TRACKER


# PATTERN LEARNED
'''
BST Strengths:
* Good performance across the board. Assuming they're balanced, binary search trees are good at lots of operations, even if they're not constant time for anything.
    - Compared to a sorted array, lookups take the same amount of time (O(lg(n))O(lg(n))), but inserts and deletes are faster (O(lg(n))O(lg(n)) for BSTs, O(n)O(n) for arrays).
    - Compared to dictionaries, BSTs have better worst case performance—O(lg(n))O(lg(n)) instead of O(n)O(n). But, on average dictionaries perform better than BSTs (meaning O(1)O(1) time complexity).
* BSTs are sorted. Taking a binary search tree and pulling out all of the elements in sorted order can be done in O(n)O(n) using an in-order traversal. Finding the element closest to a value can be done in O(lg(n))O(lg(n)) (again, if the BST is balanced!).

BST Weaknesses:
* Poor performance if unbalanced. Some types of binary search trees balance automatically, but not all. If a BST is not balanced, then operations become O(n)O(n).
* No O(1)O(1) operations. BSTs aren't the fastest for anything. On average, a list or a dictionary will be faster.
'''


# VALID BINARY SEARCH TREE
# O(n) time and O(n) space.
def is_binary_search_tree(root):

    # Determine if the tree is a valid binary search tree
    node_and_bounds_stack = [(root, -float('inf'), float('inf'))]

    while len(node_and_bounds_stack):
        node, lower_bound, upper_bound = node_and_bounds_stack.pop()

        if (node.value <= lower_bound) or (node.value >= upper_bound):
            return False

        if node.left:
            node_and_bounds_stack.append((node.left, lower_bound, node.value))
        if node.right:
            node_and_bounds_stack.append((node.right, node.value, upper_bound))

    return True

# # RECURSIVE SOLUTION
# def is_binary_search_tree(root, lower_bound=-float('inf'), upper_bound=float('inf')):
#     if not root:
#         return True

#     if (root.value >= upper_bound or root.value <= lower_bound):
#         return False

#     return (is_binary_search_tree(root.left, lower_bound, root.value)
#             and is_binary_search_tree(root.right, root.value, upper_bound))


# PATTERN LEARNED
'''
We are following a greedy approach with this one.
We are also using divide and conquer approach. Solving right and left.
'''



# FIND SECOND HIGHEST
def find_largest(root_node):
    current = root_node
    while current:
        if not current.right:
            return current.value
        current = current.right

def find_second_largest(root_node):
    if (root_node is None or
            (root_node.left is None and root_node.right is None)):
        raise ValueError('Tree must have at least 2 nodes')

    current = root_node
    while current:
        # Case: current is largest and has a left subtree
        # 2nd largest is the largest in that subtree
        if current.left and not current.right:
            return find_largest(current.left)

        # Case: current is parent of largest, and largest has no children,
        # so current is 2nd largest
        if (current.right and
                not current.right.left and
                not current.right.right):
            return current.value

        current = current.right


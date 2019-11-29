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

# PATTERN LEARNED
'''
It's very important to understand the properties of the data structure you are using.

Here we used a "simplify, solve, and adapt" strategy.
'''



# GRAPH COLORING
def color_graph(graph, colors):
    for node in graph:
        if node in node.neighbors:
            raise Exception('Legal coloring impossible for node with loop: %s' %
                            node.label)

        # Get the node's neighbors' colors, as a set so we
        # can check if a color is illegal in constant time
        illegal_colors = set([
            neighbor.color
            for neighbor in node.neighbors
            if neighbor.color
        ])

        # Assign the first legal color
        for color in colors:
            if color not in illegal_colors:
                node.color = color
                break


# proof by induction that D + 1 is always enough for legal coloring
'''
In general, an inductive proof uses 2 steps to prove a claim is true for all (usually positive) integers:

1. A base case showing the claim is true for the first number (1 or 0)
2. An inductive step showing that if we assume the claim is true for a number nn, then the claim is also true for n+1n+1

If the claim is true for the first number, and for any next number, then it must be true for all numbers.

So let's prove this claim:

A legal coloring with D+1 colors is always possible for a graph of N nodes with maximum degree D.

For our base case, we need to show this claim holds for a graph with 1 node.

A graph with 1 node has 0 edges, so the maximum degree DD is 0. That means we have 1 color (D+1=1D+1=1).

Can we color that node with the one available color? Definitely, since it doesn't have any adjacent nodes that could make the coloring illegal.

""What about if the graph has a loop! ↴ We're assuming our graph doesn't have these because otherwise, there's no possible legal coloring. Keep this edge case in mind though: we'll need to check for loops in our input graph and throw an error if we find any.""

So we've proven our base case. Now for the inductive step.

This'll be our assumption:

A D+1 coloring is possible for a graph with N nodes.

Can we show that if our assumption is true, it must also be true for a graph with N+1N+1 nodes?

Let's say we have a graph with N+1 nodes and maximum degree D. We're not sure yet if we can color it with D+1 colors, right?

Ok, so let's remove a node and its edges from the graph. Any node. Now we have a graph with N nodes.

What happened to D by removing a node?

D either stayed the same or went down. We removed edges, so there's no way D went up.

So now we have a graph with N nodes and maximum degree at most D. Can we color this graph with D+1 colors?

Yup! That's exactly our assumption! As part of the inductive step, we've assumed that we can color this graph with D+1 colors. So let's go ahead and color the graph.

Now all we have to do is add back in the node we removed (so we have N+1 nodes again) and show we can find a valid color for that node.

When we add the node we removed back in, what's the most neighbors it can have?

D. We started with a graph with N+1 nodes and maximum degree D, and we just rebuilt that graph.

In the worst case, the node we add back in will have D neighbors, and they'll all have different colors. Not a problem. We have D+1 colors to choose from, so at least one color is still free. We'll use that one for this node. Bam.
'''
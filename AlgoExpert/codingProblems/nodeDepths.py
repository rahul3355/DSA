def nodeDepths(root, depth=0):
    
    # O(n) time | O(h) space, where h is the height of tree
    
    # handle base case of recursion
    if root is None:
        return 0
    return depth + nodeDepths(root.left, depth+1) + nodeDepths(root.right, depth+1)
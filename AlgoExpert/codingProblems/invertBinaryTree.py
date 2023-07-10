def invertBinaryTree(tree):
    # Write your code here.
    if tree is None:
        return
    swapLeftandRight(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)

def swapLeftandRight(tree):
    tree.left, tree.right = tree.right, tree.left
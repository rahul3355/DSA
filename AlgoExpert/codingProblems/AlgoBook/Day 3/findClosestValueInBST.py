def findClosestValueInBst(tree, target):
    # O(log(N)) time | O(1) space
    currentNode = tree
    minDifference = abs(currentNode.value - target)
    closestValueInBST = currentNode.value
    while currentNode is not None:
        if currentNode.value < target:
            newDifference = abs(currentNode.value - target)
            if newDifference < minDifference:
                minDifference = newDifference
                closestValueInBST = currentNode.value
            currentNode = currentNode.right
            
        elif currentNode.value > target:
            newDifference = abs(currentNode.value - target)
            if newDifference < minDifference:
                minDifference = newDifference
                closestValueInBST = currentNode.value
            currentNode = currentNode.left
            
        else:
            return currentNode.value
    return closestValueInBST


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

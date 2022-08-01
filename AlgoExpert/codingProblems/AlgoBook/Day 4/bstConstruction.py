# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.

        # O(log(N)) time | O(1) space
        currentNode = self
        while True:
            if value >= currentNode.value:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
            else:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
        
        # Do not edit the return statement of this method.
        return self

    def contains(self, value):
        # O(log(N)) time | O(1) space
        currentNode = self
        while currentNode is not None:
            if value > currentNode.value:
                currentNode = currentNode.right
            elif value < currentNode.value:
                currentNode = currentNode.left
            else:
                return True
        return False

    def remove(self, value, parentNode = None):
        # Write your code here.

        # O(log(N)) time | O(1) space
        currentNode = self
        while currentNode is not None:
            if value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            elif value < currentNode.left:
                parentNode = currentNode
                currentNode = currentNode.left
            else:
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinVal()
                    currentNode.right.remove(currentNode.value, currentNode)
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.rigt is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.left.right
                        currentNode.right = currentNode.right.right
                    else:
                        pass
                if parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.right if currentNode.left is not None else currentNode.right
                break
        
        # Do not edit the return statement of this method.
        return self
 
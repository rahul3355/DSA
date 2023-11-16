class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0

        maxDepthoftree = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        return maxDepthoftree
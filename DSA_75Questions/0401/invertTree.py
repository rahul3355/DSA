class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        root.left, root.right = root.right, root.left
        
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root
        
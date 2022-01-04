class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = [root.val]
        
        #return max path without split
        def dfs(root):
            if not root:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            
            # compute max path sum with split
            res[0] = max(res[0], root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)
    
        dfs(root)
        return res[0]
            
        
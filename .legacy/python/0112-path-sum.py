class Solution:
    # O(n) time | O(d) space
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: 
            return False
        targetSum -= root.val
        if not root.left and not root.right:
            return targetSum == 0
        if self.hasPathSum(root.left, targetSum):
            return True
        if self.hasPathSum(root.right, targetSum):
            return True
        return False
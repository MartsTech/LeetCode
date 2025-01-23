class Solution:
    # O(n) time | O(h) space
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], num: int) -> int:
            if not node: 
                return 0
            num = num * 10 + node.val
            if not node.left and not node.right:
                return num
            return dfs(node.left, num) + dfs(node.right, num)
        return dfs(root, 0)        
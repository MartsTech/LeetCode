class Solution:
    # O(n) time | O(h) space
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)
            res[0] = max(res[0], node.val + leftMax + rightMax)
            return node.val + max(leftMax, rightMax)
        dfs(root)
        return res[0]
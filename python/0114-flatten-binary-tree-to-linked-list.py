class Solution:
    # O(n) time | O(h) space
    def flatten(self, root: Optional[TreeNode]) -> None:
        def dfs(root: Optional[TreeNode]) ->  Optional[TreeNode]:
            if not root: return root
            ltail = dfs(root.left)
            rtail = dfs(root.right)
            if root.left:
                ltail.right = root.right
                root.right = root.left
                root.left = None
            return rtail or ltail or root
        dfs(root)
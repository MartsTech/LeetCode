class Solution:
    # O(n) time | O(n) space
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        hashmap = {v: i for i, v in enumerate(inorder)}
        def helper(l: int, r: int) -> Optional[TreeNode]:
            if l > r: return None
            root = TreeNode(postorder.pop())
            idx = hashmap[root.val]
            root.right = helper(idx + 1, r)
            root.left = helper(l, idx - 1)
            return root
        return helper(0, len(inorder) - 1)
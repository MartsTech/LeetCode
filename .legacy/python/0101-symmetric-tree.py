class Solution:
    # O(n) time | O(d) space
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return False
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
        return True
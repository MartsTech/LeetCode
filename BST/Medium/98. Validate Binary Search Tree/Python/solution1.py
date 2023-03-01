# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) time | O(d) space
    def isValidBST(self, root: Optional[TreeNode], min = float('-inf'), max = float('inf')) -> bool:
        if not root:
            return True

        if root.val <= min or root.val >= max:
            return False

        left = self.isValidBST(root.left, min, root.val)
        right = self.isValidBST(root.right, root.val, max)

        return left and right
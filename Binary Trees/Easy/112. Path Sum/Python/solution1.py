# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) time | O(n) space
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.hasPathSumHelper(root, targetSum, 0)

    def hasPathSumHelper(self, node: Optional[TreeNode], targetSum: int, sum: int) -> bool:
        if not node:
            return False
        sum += node.val
        if sum == targetSum and not node.left and not node.right:
            return True
        if self.hasPathSumHelper(node.left, targetSum, sum):
            return True
        if self.hasPathSumHelper(node.right, targetSum, sum):
            return True
        return False
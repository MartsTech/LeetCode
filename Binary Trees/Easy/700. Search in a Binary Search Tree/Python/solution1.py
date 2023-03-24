# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(log(n)) time | O(h) space
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return
        if root.val < val:
            root = root.right
        elif root.val > val:
            root = root.left
        else:
            return root
        return self.searchBST(root, val)
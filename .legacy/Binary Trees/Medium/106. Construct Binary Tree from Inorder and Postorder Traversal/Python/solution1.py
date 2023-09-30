# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n^2) time | O(n) space
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        root_val = postorder[-1]
        root_idx = inorder.index(root_val)

        left_inorder = inorder[:root_idx]
        right_inorder = inorder[root_idx+1:]

        left_postorder = postorder[:root_idx]
        right_postorder = postorder[root_idx:-1]

        left_subtree = self.buildTree(left_inorder, left_postorder)
        right_subtree = self.buildTree(right_inorder, right_postorder)

        return TreeNode(root_val, left_subtree, right_subtree)
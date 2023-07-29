# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) time | O(h) space - where n is the number of nodes and h is the heigth of the tree
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        array = []
        self.traverse(root, array)
        return array

    def traverse(self, node: Optional[TreeNode], array: List[int]) -> None:
        if not node:
            return
        self.traverse(node.left, array)
        self.traverse(node.right, array)
        array.append(node.val)
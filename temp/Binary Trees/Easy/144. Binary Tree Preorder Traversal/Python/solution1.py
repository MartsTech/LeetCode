# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) time | O(h) space - where n is the number of nodes and h is the height of the tree
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        array = []
        self.traverse(root, array)
        return array

    def traverse(self, node: Optional[TreeNode], array: List[int]) -> None:
        if not node:
            return
        array.append(node.val)
        self.traverse(node.left, array)
        self.traverse(node.right, array)
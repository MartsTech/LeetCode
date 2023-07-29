# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) time | O(n) space
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        return self.findTargetHelper(root, k, {})

    def findTargetHelper(self, node: Optional[TreeNode], k: int, nodes: Dict[int, bool]) -> bool:
        if not node:
            return False
        target = k - node.val
        if target in nodes:
            return True
        nodes[node.val] = True
        if self.findTargetHelper(node.left, k, nodes):
            return True
        if self.findTargetHelper(node.right, k, nodes):
            return True
        return False
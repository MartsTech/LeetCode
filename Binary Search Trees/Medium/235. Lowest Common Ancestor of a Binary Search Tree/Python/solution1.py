# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # O(logn) time | O(h) space
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        return self.traverse(root, p, q)

    def traverse(self, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val <= node.val <= q.val:
            return node
        elif q.val < node.val:
            return self.traverse(node.left, p, q)
        else:
            return self.traverse(node.right, p, q)

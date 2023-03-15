# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) time | O(n) space
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = deque([root])
        end_reached = False
        while queue:
            node = queue.popleft()
            if not node:
                end_reached = True
            else:
                if end_reached:
                    return False
                queue.append(node.left)
                queue.append(node.right)
        return True
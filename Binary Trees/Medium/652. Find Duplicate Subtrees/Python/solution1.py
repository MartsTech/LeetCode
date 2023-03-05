# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) time | O(n) space
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        result = []
        cache = {}
        self.traverse(result, cache, root)
        return result

    def traverse(self, result, cache, root):
        if not root:
            return ""

        left = self.traverse(result, cache, root.left)
        right = self.traverse(result, cache, root.right)
        current = str(root.val) + "$" + left + "$" + right

        if current not in cache:
            cache[current] = 0 
        elif cache[current] == 1:
            result.append(root)

        cache[current] += 1

        return current
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    # O(n) time | O(n) space
    def preorder(self, root: 'Node') -> List[int]:
        array = []
        self.traverse(root, array)
        return array

    def traverse(self, node: 'Node', array: List[int]) -> List[int]:
        if node == None:
            return

        array.append(node.val)

        for child in node.children:
            self.traverse(child, array)
        
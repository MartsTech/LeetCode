"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    # O(n^2logn) time | O(n^2) space
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        if n == 0: return None
        return self.construct_helper(grid, 0, 0, n - 1, n - 1)

    def construct_helper(self, grid: List[List[int]], x1: int, y1: int, x2: int, y2: int) -> 'Node':
        if x1 == x2 and y1 == y2:
            return Node(grid[x1][y1], True, None, None, None, None)

        mid_x = (x1 + x2) // 2
        mid_y = (y1 + y2) // 2

        top_left = self.construct_helper(grid, x1, y1, mid_x, mid_y)
        top_right = self.construct_helper(grid, x1, mid_y + 1, mid_x, y2)
        bottom_left = self.construct_helper(grid, mid_x + 1, y1, x2, mid_y)
        bottom_right = self.construct_helper(grid, mid_x + 1, mid_y + 1, x2, y2)

        if top_left.isLeaf and top_right.isLeaf and bottom_left.isLeaf and bottom_right.isLeaf and top_left.val == top_right.val == bottom_left.val == bottom_right.val:
            return Node(top_left.val, True, None, None, None, None)
        else:
            return Node(None, False, top_left, top_right, bottom_left, bottom_right)

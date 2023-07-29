import math

class Solution:
    # O(1) time | O(1) space
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(n + m - 2, n - 1)
class Solution:
    # O(n) time | O(1) space
    def climbStairs(self, n: int) -> int:
        if n < 4: return n
        steps = [1, 2]
        for _ in range(3, n):
            steps[0], steps[1] = steps[1], steps[0] + steps[1]
        return steps[0] + steps[1]
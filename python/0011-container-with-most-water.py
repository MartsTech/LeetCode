class Solution:
    # O(n) time | O(1) space
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            h = min(height[l], height[r])
            w = r - l
            res = max(res, h * w)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
class Solution:
    # O(n) time | O(1) space 
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        result = 0
        min_pos = -1
        max_pos = -1
        left_bound = -1
        for idx, num in enumerate(nums):
            if num < minK or num > maxK:
                left_bound = idx
            if num == minK:
                min_pos = idx
            if num == maxK:
                max_pos = idx
            result += max(0, min(min_pos, max_pos) - left_bound)
        return result
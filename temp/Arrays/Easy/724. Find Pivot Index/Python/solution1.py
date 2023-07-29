class Solution:
    # O(n) time | O(1) space
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        for idx, num in enumerate(nums):
            right -= num
            if left == right:
                return idx
            left += num
        return -1
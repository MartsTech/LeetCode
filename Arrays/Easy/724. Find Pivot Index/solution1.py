class Solution:
    # O(n) time | O(1) space
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        for idx in range(len(nums)):
            right -= nums[idx]
            if left == right:
                return idx
            left += nums[idx]
        return -1
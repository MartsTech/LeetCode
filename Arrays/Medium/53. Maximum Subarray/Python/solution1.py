class Solution:
    # O(n) time | O(1) space
    def maxSubArray(self, nums: List[int]) -> int:
        prev_sum = nums[0]
        max_sum = nums[0]
        for idx in range(1, len(nums)):
            num = nums[idx]
            prev_sum = max(num, prev_sum + num)
            max_sum = max(max_sum, prev_sum)
        return max_sum
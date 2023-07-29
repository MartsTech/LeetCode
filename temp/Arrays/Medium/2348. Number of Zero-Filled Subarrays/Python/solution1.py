class Solution:
    # O(n) time | O(1) space
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] == 0:
                count += right - left + 1
            else:
                left = right + 1
            right += 1
        return count
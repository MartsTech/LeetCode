class Solution:
    # O(n) time | O(1) space
    def moveZeroes(self, nums: List[int]) -> None:
        left = right = 0
        while left < len(nums):
            if nums[left] != 0:
                nums[right] = nums[left]
                right += 1
            left += 1
        while right < len(nums):
            nums[right] = 0
            right += 1
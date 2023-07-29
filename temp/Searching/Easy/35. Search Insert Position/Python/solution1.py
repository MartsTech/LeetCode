class Solution:
    # O(log(n)) time | O(1) space
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            middle = (left + right) // 2
            num = nums[middle]
            if num < target:
                left = middle + 1
            elif num > target:
                right = middle
            else:
                return middle
        return left
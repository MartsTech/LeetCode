class Solution:
    # O(log(n)) time | O(1) space
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            num = nums[middle]
            if num == target:
                return middle
            elif num < target:
                left = middle + 1
            else:
                right = middle - 1
        return -1
            
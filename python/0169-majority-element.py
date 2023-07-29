class Solution:
    # O(n) time | O(1) space
    def majorityElement(self, nums: List[int]) -> int:
        val, count = nums[0], 0
        for num in nums:
            if num == val:
                count += 1
            else:
                count -= 1
                if count == 0:
                    val = num
                    count = 1
        return val
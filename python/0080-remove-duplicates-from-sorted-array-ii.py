class Solution:
    # O(n) time | O(1) space
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        val, count = nums[0], 0
        for num in nums:
            if num == val:
                count += 1
            else:
                val = num
                count = 1
            if count <= 2:
                nums[k] = num
                k += 1
        return k
class Solution:
    # O(n) time | O(1) space
    def runningSum(self, nums: List[int]) -> List[int]:
        for idx in range(len(nums)):
            if idx == 0:
                continue
            nums[idx] = nums[idx] + nums[idx - 1]
        return nums

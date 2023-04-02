class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack(0, nums, result)
        return result

    def backtrack(self, first: int, nums: List[int], result: List[List[int]]) -> None:
        if first == len(nums):
            result.append(nums[:])
        for i in range(first, len(nums)):
            nums[first], nums[i] = nums[i], nums[first]
            self.backtrack(first + 1, nums, result)
            nums[first], nums[i] = nums[i], nums[first]
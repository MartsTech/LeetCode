class Solution:
    # O(n) time | O(n) space
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            match  = target - nums[i]
            if match in hashmap:
                return [hashmap[match], i]
            hashmap[nums[i]] = i
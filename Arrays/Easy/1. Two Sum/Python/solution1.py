class Solution:
    # O(n) time | O(n) space
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for idx, num in enumerate(nums):
            match = target - num
            if match in cache:
                return [cache[match], idx]
            cache[num] = idx
        return []
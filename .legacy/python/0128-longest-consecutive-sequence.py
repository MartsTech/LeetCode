class Solution:
    # O(n) time | O(1) space
    def longestConsecutive(self, nums: List[int]) -> int:
        res, hashset = 0, set(nums)
        for num in nums:
            if num - 1 in hashset:
                continue
            count = 0
            while num + count in hashset:
                count += 1
            res = max(res, count)
        return res
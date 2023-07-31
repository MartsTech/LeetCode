class Solution:
    # O(n) time | O(1) space
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        res = []
        l = r = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[r] + 1:
                r += 1
                continue
            if l != r:
                res.append(f"{nums[l]}->{nums[r]}")
            else:
                res.append(f"{nums[l]}")
            l = r = i
        if l != r:
            res.append(f"{nums[l]}->{nums[r]}")
        else:
            res.append(f"{nums[l]}")
        return res
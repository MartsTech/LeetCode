class Solution:
    # O(n) time | O(1) space 
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        pre = post = 1
        for i in range(n):
            res[i] *= pre
            pre *= nums[i]
            res[n - i - 1] *= post
            post *= nums[n - i - 1]
        return res
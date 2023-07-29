class Solution:
    # O(n) time | O(n) space
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n + 1)]
        dp[1] = nums[0]
        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        return dp[n]
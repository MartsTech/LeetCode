class Solution:
    # O(n) time | O(1) space
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        if k == n: return nums
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
        return nums
        
    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
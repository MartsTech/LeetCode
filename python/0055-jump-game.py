class Solution:
    # O(n) time | O(1) space
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for idx in range(goal, -1, -1):
            if idx + nums[idx] >= goal:
                goal = idx
        return goal == 0
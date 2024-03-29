class Solution {
public:
    // O(n) time | O(1) space
    std::vector<int> runningSum(std::vector<int>& nums) {
        size_t n = nums.size();
        for (size_t i = 1; i < n; ++i) {
            nums[i] += nums[i - 1];
        }
        return nums;
    }
};
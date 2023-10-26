class Solution {
public:
    // O(n) time | O(1) space - n is the length of nums
    vector<int> runningSum(vector<int>& nums) {
        int n = nums.size();
        for (int i = 1; i < n; ++i) {
            nums[i] += nums[i - 1];
        }
        return nums;
    }
};
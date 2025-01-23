class Solution {
public:
    // O(nlogn) time | O(logn) space
    int minPairSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int maxSum = INT_MIN, n = nums.size();
        for(int i = 0; i < n / 2; ++i) {
            maxSum = max(maxSum, nums[i] + nums[n - i - 1]);
        }
        return maxSum;
    }
};
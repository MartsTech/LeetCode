class Solution {
public:
    // O(nlogn) time | O(logn) space
    int reductionOperations(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int res = 0, up = 0, n = nums.size();
        for (int i = 1; i < n; ++i) {
            if (nums[i] != nums[i - 1]) {
                ++up;
            }
            res += up;
        }
        return res;
    }
};
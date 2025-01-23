class Solution {
public:
    // O(nlogn) time | O(logn) space
    int maxFrequency(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int n = nums.size(), l = 0;
        long curr = 0;
        for (int r = 0; r < n; ++r) {
            long target = nums[r];
            curr += target;
            if ((r - l + 1) * target - curr > k) {
                curr -= nums[l++];
            }
        }
        return n - l;
    }
};
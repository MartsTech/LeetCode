class Solution {
public:
    // O(logn) time | O(1) space
    int searchInsert(vector<int>& nums, int target) {
        int l = 0, r = nums.size();
        while (l < r) {
            int k = (l + r) / 2;
            if (nums[k] < target) {
                l = k + 1;
            } else if (nums[k] > target) {
                r = k;
            } else {
                return k;
            }
        }
        return l;
    }
};
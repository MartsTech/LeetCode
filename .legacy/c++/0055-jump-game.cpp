class Solution {
public:
    // O(n) time, O(1) space - where n is the size of the input array
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        int res = n - 1;
        for (int i = n - 2; i >= 0; --i) {
            if (nums[i] + i >= res) {
                res = i;
            }
        }
        return res == 0;
    }
};
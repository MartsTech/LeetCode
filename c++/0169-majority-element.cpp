class Solution {
public:
    // O(n) time, O(1) space - where n is the size of the input array
    int majorityElement(vector<int>& nums) {
        int res = nums[0], count = 1;
        int n = nums.size();
        for (int i = 1; i < n; ++i) {
            if (nums[i] != res) {
                --count;
            }
            if (count == 0) {
                res = nums[i];
                count = 1;
            }
        }
        return res;
    }
};
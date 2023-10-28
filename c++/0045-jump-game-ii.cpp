class Solution {
public:
    // O(n) time, O(1) space - where n is the size of the input array
    int jump(vector<int>& nums) {
        int res = 0;
        int l = 0, r = 0;
        int n = nums.size();
        while (r < n - 1) {
            int jump = 0;
            for (int i = l; i < r + 1; ++i) {
                jump = max(jump, i + nums[i]);
            }
            l = r + 1;
            r = jump;
            ++res;
        }
        return res;
    }
};
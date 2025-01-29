class Solution {
public:
    // O(n) time | O(1) space
    int removeDuplicates(vector<int>& nums) {
        int k = 1;
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i - 1] != nums[i]) {
                nums[k++] = nums[i];
            }
        }
        return k;
    }
};
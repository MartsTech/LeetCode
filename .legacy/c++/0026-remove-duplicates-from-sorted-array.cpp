class Solution {
public:
    // O(n) time, O(1) space - where n is the size of the array
    int removeDuplicates(vector<int>& nums) {
        int k = 1, n = nums.size();
        for (int i = 1; i < n; ++i) {
            if (nums[i] != nums[i - 1]) {
                nums[k++] = nums[i];
            }
        }
        return k;
    }
};
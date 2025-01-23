class Solution {
public:
    // O(n) time, O(1) space - where n is the size of the array
    int removeElement(vector<int>& nums, int val) {
        int k = 0;
        for (int num : nums) {
            if (num != val) {
                nums[k++] = num;
            }
        }
        return k;
    }
};
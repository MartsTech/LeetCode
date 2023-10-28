class Solution {
public:
    // O(n) time, O(1) space - where n is the size of the array
    int removeDuplicates(vector<int>& nums) {
        int k = 0;
        int val = nums[0], count = 0;
        for (int num : nums) {
            if (num == val) {
                ++count;
            } else {
                val = num;
                count = 1;
            }
            if (count <= 2) {
                nums[k++] = num;
            } 
        }
        return k;
    }
};
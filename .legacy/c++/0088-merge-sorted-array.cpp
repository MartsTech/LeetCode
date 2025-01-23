class Solution {
public:
    // O(m + n) time, O(1) space - where m and n are the sizes of the arrays
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        while (n > 0) {
            if (m > 0 && nums1[m - 1] > nums2[n - 1]) {
                nums1[n + m - 1] = nums1[m - 1];
                m -= 1;
            } else {
                nums1[n + m - 1] = nums2[n - 1];
                n -= 1;
            }
        }
    }
};
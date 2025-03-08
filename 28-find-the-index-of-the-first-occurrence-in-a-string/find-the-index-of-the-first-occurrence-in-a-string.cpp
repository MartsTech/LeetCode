class Solution {
public:
    // O((n - m) * m) time | O(1) space
    int strStr(string haystack, string needle) {
        int n = haystack.size(), m = needle.size();
        if (m == 0) return -1;
        for (int i = 0; i < n - m + 1; ++i) {
            int j = 0;
            while (j < m && haystack[i + j] == needle[j] && ++j);
            if (j == m) return i;
        }
        return -1;
    }
};
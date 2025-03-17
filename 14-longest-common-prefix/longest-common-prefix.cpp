class Solution {
public:
    // O(m + n log n) time | O(1) space
    string longestCommonPrefix(vector<string>& strs) {
        sort(strs.begin(), strs.end());
        string& left = strs[0], right = strs.back();
        int k = 0;
        while (k < min(left.size(), right.size()) && left[k] == right[k]) ++k;
        return left.substr(0, k);
    }
};
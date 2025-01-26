class Solution {
public:
    // 0(m * n log n) | O(1) space
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.size() == 0) return "";
        sort(strs.begin(), strs.end());
        string& first = strs[0], last = strs.back();
        int i = 0;
        while (i < first.size() && i < last.size() && first[i] == last[i]) ++i;
        return first.substr(0, i);
    }
};
class Solution {
public:
    // O(n) time | O(1) space
    int lengthOfLastWord(string s) {
        int r = s.length() - 1;
        while (r >= 0 && s[r] == ' ') --r;
        int l = r;
        while (l >= 0 && s[l] != ' ') --l;
        return r - l;
    }
};
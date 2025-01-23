class Solution {
public:
    // O(n) time || O(n) space
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        std::unordered_map<char, int> freq;
        for (char c : s) {
            ++freq[c];
        } 
        for (char c : t) {
            if (--freq[c] < 0) {
                return false;
            }
        }
        return true;
    }
};
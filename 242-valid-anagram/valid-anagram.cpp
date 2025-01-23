class Solution {
public:
    // O(n log n) time || O(1) space
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
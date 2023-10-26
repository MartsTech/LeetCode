class Solution {
public:
    // O(m + n) time | O(m) space - where m is the length of the magazine
    // and n is the length of the ransom note
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> hashmap;
        for (char c : magazine) {
            ++hashmap[c];
        }
        for (char c : ransomNote) {
            if (!hashmap[c]) {
                return false;
            }
            --hashmap[c];
        }
        return true;
    }
};
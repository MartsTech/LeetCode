class Solution {
public:
    // O(m + n) time | O(n) space
    bool canConstruct(string ransomNote, string magazine) {
        int m = ransomNote.size(), n = magazine.size();
        if (m > n) {
            return false;
        }
        unordered_map<char, int> letters;
        for (char l : magazine) {
            ++letters[l];
        }
        for (char l : ransomNote) {
            if (!letters[l]) {
                return false;
            }
            --letters[l];
        }
        return true;
    }
};
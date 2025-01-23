class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string result;
        int m = word1.size(), n = word2.size();
        int size = max(m, n);
        for (int i = 0; i < size; ++i) {
            if (i < m) {
                result += word1[i];
            }
            if (i < n) {
                result += word2[i];
            }
        }
        return result; 
    }
};
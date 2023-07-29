class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int n = word1.size();
        int m = word2.size();
        string result = string(n + m, ' ');
        int i = 0;
        int j = 0;
        while (i < n && j < m) {
            result[i + j] = word1[i];
            result[i + j + 1] = word2[j];
            i++;
            j++;
        }
        while (i < n) {
            result[i + j] = word1[i];
            i++;
        }
        while (j < m) {
            result[i + j] = word2[j];
            j++;
        }
        return result;
    }
};
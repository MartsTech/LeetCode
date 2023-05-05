class Solution {
public:
    int maxVowels(string s, int k) {
        int res = 0;
        int count = 0;
        for (int i = 0; i < k; i++) {
            if (isVowel(s[i])) {
                count++;
            }
        }
        res = count;
        for (int i = k; i < s.size(); i++) {
            if (isVowel(s[i])) {
                count++;
            }
            if (isVowel(s[i - k])) {
                count--;
            }
            res = max(res, count);
        }
        return res;
    }
private:
    bool isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' ||c == 'o' || c == 'u';
    }
};
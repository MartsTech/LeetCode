class Solution {
public:
    // O(n) time | O(1) space
    int romanToInt(string s) {
        unordered_map<char, int> map = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };
        int res = 0, n = s.size();
        for (int i = 0; i < n; ++i) {
            if (i + 1 < n && map[s[i]] < map[s[i + 1]]) {
                res += map[s[i + 1]] - map[s[i++]];
            } else {
                res += map[s[i]];
            }
        }
        return res;
    }
};
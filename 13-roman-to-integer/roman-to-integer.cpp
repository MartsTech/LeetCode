class Solution {
public:
    unordered_map<char, int> map = {
        {'I', 1},
        {'V', 5},
        {'X', 10},
        {'L', 50},
        {'C', 100},
        {'D', 500},
        {'M', 1000}
    };

    // O(n) time | O(1) space
    int romanToInt(string s) {
        int num = 0;
        for (int i = 0; i < s.size(); ++i) {
            if (i + 1 < s.size() && map[s[i]] < map[s[i + 1]]) {
                num += map[s[i + 1]] - map[s[i++]];
            } else {
                num += map[s[i]];
            }
        }
        return num;
    }
};
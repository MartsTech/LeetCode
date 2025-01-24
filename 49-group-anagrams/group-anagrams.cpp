class Solution {
public:
    // O(n * m log m) time | O(n * m) space
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map;
        for (string& str : strs) {
            string key = str;
            sort(key.begin(), key.end());
            map[key].push_back(str);
        }
        vector<vector<string>> groups;
        for (auto& pair : map) {
            groups.push_back(pair.second);
        }
        return groups;
    }
};
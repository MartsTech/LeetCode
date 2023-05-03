class Solution {
public:
    vector<vector<int>> findDifference(vector<int> &nums1, vector<int> &nums2) {
        vector<vector<int>> res = {{}, {}};
        unordered_set<int> unique1 = {nums1.begin(), nums1.end()};
        unordered_set<int> unique2 = {nums2.begin(), nums2.end()};
        for (auto &n: unique1) {
            if (unique2.find(n) == unique2.end()) {
                res[0].push_back(n);
            }
        }
        for (auto &n: unique2) {
            if (unique1.find(n) == unique1.end()) {
                res[1].push_back(n);
            }
        }
        return res;
    }
};
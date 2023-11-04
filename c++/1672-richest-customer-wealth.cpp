class Solution {
public:
    // O(m*n) time, O(1) space
    int maximumWealth(vector<vector<int>>& accounts) {
        int max_wealth = 0;
        size_t m = accounts.size(), n = accounts[0].size();
        for (size_t i = 0; i < m; ++i) {
            int wealth = 0;
            for (size_t j = 0; j < n; ++j) {
                wealth += accounts[i][j];
            }
            max_wealth = max(max_wealth, wealth);
        }
        return max_wealth;
    }
};
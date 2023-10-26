class Solution {
public:
    // O(m*n) time | O(1) space - m is the number of customers, n is the number of banks
    int maximumWealth(vector<vector<int>>& accounts) {
        int res = 0;
        int m = accounts.size();
        int n = accounts[0].size();
        for (int i = 0; i < m; ++i) {
            int wealth = 0;
            for (int j = 0; j < n; ++j) {
                wealth += accounts[i][j];
            }
            res = max(res, wealth);
        }
        return res;
    }
};
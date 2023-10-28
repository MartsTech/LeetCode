class Solution {
public:
    // O(n) time, O(1) space - where n is the size of the input array
    int maxProfit(vector<int>& prices) {
        int res = 0, n = prices.size();
        for (int i = 1; i < n; ++i) {
            if (prices[i] > prices[i - 1]) {
                res += (prices[i] - prices[i - 1]);
            }
        }
        return res;
    }
};
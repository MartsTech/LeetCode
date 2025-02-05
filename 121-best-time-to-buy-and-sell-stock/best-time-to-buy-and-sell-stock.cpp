class Solution {
public:
    // O(n) time | O(1) space
    int maxProfit(vector<int>& prices) {
        int min = INT_MAX;
        int max = INT_MIN;
        for (int price : prices) {
            min = std::min(price, min);
            max = std::max(max, price - min);
        }
        return max;
    }
};
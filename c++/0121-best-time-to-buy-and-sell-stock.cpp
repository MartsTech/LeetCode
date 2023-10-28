class Solution {
public:
    // O(n) time, O(1) space - where n is the size of the input array
    int maxProfit(vector<int>& prices) {
        int res = 0;
        int minPrice = numeric_limits<int>::max();
        int maxPrice = numeric_limits<int>::min();
        for (int price : prices) {
            if (price < minPrice) {
                minPrice = price;
                maxPrice = price;
            }
            if (price > maxPrice) {
                maxPrice = price;
                int profit = maxPrice - minPrice;
                if (profit > res) {
                    res = profit;
                }
            }
        }
        return res;
    }
};
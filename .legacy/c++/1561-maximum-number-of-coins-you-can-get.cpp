class Solution {
public:
    // O(nlogn) time | O(logn) space
    int maxCoins(vector<int>& piles) {
        sort(piles.begin(), piles.end(), greater());
        int res = 0, n = piles.size() / 3 * 2;
        for (int i = 1; i < n; i += 2) {
            res += piles[i];
        }
        return res;
    }
};
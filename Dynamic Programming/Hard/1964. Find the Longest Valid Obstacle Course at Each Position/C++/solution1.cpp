class Solution {
public:
    vector<int> longestObstacleCourseAtEachPosition(vector<int>& obstacles) {
        int n = obstacles.size();
        vector<int> res = vector<int>(n, 0);
        vector<int> dp;
        for (int i = 0; i < n; ++i) {
            int num = obstacles[i];
            int idx = upper_bound(dp.begin(), dp.end(), num) - dp.begin();
            if (idx == dp.size()) {
                dp.push_back(num);
            } else {
                dp[idx] = num;
            }
            res[i] = idx + 1;
        }
        return res;
    }
};
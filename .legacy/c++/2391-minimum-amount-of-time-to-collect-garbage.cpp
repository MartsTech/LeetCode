class Solution {
public: 
    // O(n * m) time | O(1) space - where n is the lenght of garbage 
    // and m is the lenght of the max element of garbage
    int garbageCollection(vector<string>& garbage, vector<int>& travel) {
        int res = 0, n = garbage.size();
        unordered_map<char, int> trucks = {{'M', 0}, {'P', 0}, {'G', 0}};
        for (int i = 0; i < n; ++i) {
            for (char c : garbage[i]) {
                res += trucks[c] + 1;
                trucks[c] = 0;
            }
            int time = travel[min(i, n - 2)];
            for (auto& truck : trucks) {
                truck.second += time;
            }
        }
        return res;
    }
};
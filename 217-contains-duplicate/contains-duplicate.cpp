class Solution {
public:
    // O(n) time | O(n) space
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> set;
        for (int num : nums) {
            if (set.find(num) != set.end()) {
                return true;
            }
            set.insert(num);
        }
        return false;
    }
};
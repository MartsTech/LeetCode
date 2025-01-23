class Solution {
public:
    // O(n^2) time | O(1) space
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> seen;
        for (int i = 0; i < nums.size(); ++i) {
            if (seen.find(target - nums[i]) != seen.end()) {
                return {i, seen[target - nums[i]]};
            }
            seen[nums[i]] = i;
        }
        return {};
    }
};
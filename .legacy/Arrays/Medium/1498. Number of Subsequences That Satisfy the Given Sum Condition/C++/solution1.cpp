class Solution
{
public:
    int numSubseq(vector<int> &nums, int target)
    {
        int res = 0;
        int mod = 1e9 + 7;
        sort(nums.begin(), nums.end());
        int left = 0, right = nums.size() - 1;
        vector<int> pow(nums.size(), 1);
        for (int i = 1; i < nums.size(); i++)
        {
            pow[i] = (pow[i - 1] * 2) % mod;
        }
        while (left <= right)
        {
            if (nums[left] + nums[right] > target)
            {
                right--;
            }
            else
            {
                res = (res + pow[right - left]) % mod;
                left++;
            }
        }
        return res;
    }
};
class Solution {
public:
    // O(log(x)) | O(1) - where x is the input number
    int reverse(int x) {
        int res = 0;
        int min = INT_MIN / 10, max = INT_MAX / 10;
        while (x) {
            if (res > max || res < min) {
                return 0;
            }
            res = res * 10 + x % 10;
            x /= 10;
        }
        return res;
    }
};
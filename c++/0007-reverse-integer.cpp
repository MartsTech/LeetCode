class Solution {
public:
    // O(n) time, O(1) space - n is the number of digits
    int reverse(int x) {
        long res = 0;
        while (x) {
            res *= 10;
            res += x % 10;
            x /= 10;
        }
        if (res > INT_MAX || res < INT_MIN) {
            return 0;
        }
        return res;
    }
};
class Solution {
public:
    // O(log n)) time | O(1) space
    bool isPalindrome(int x) {
        if (x < 0) return 0;
        int tmp = x;
        long rev = 0;
        while (tmp) {
            rev *= 10;
            rev += tmp % 10;
            tmp /= 10;
        }
        return x == rev;
    }
};
class Solution {
public:
    // O(logn) time | O(1) space
    bool isPalindrome(int x) {
        if (x < 0) return false;
        long rev = 0;
        int temp = x;
        while (temp) {
            rev *= 10;
            rev += temp % 10;
            temp /= 10;
        }
        return x == rev;
    }
};
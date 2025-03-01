class Solution {
public:
    // O(log n) time | O(1) space 
    bool isPalindrome(int x) {
        if (x < 0) return false;
        int num = x;
        long rev = 0;
        while (num) {
            rev *= 10;
            rev += num % 10;
            num /= 10;
        }
        return x == rev;
    }
};
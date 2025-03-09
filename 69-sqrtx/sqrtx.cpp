class Solution {
public:
    // O(sqrt x) time | O(1) space
    int mySqrt(int x) {
        if (x == 0) return 0;
        long i = 1;
        while (i * i <= x) ++i;
        return i - 1;
    }
};
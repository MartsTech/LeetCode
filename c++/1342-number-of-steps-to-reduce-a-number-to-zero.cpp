class Solution {
public:
    // O(log(n)) time | O(1) space - where n is the input number
    int numberOfSteps(int num) {
        int res = 0;
        while (num) {
            if (num % 2 == 0) {
                num /= 2;
            } else {
                num -= 1;
            }
            ++res;
        }
        return res;
    }
};
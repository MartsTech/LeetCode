class Solution {
public:
    // O(log(num)) time | O(1) space
    int numberOfSteps(int num) {
        int steps = 0;
        while (num) {
            if (num % 2 == 0) {
                num /= 2;
            } else {
                num -= 1;
            }
            ++steps;
        }
        return steps;   
    }
};
class Solution {
public:
    unordered_map<char, char> map = {
        {')', '('},
        {'}', '{'},
        {']', '['}
    };

    // O(n) time | O(n) space
    bool isValid(string s) {
        stack<char> stack;
        for (char c : s) {
            if (map.find(c) == map.end()) { 
                stack.push(c);
                continue;
            }
            if (!stack.empty() && stack.top() == map[c]) {
                stack.pop();
                continue;
            }
            return false;
        }
        return stack.empty();
    }
};
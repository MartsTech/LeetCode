class Solution {
public:
    // O(max(n, m)) time | O(max(n, m)) space
    string addBinary(string a, string b) {
        int i = a.size() - 1, j = b.size() - 1;
        int carry = 0;
        string res;
        while (i >= 0 || j >= 0 || carry > 0) {
            int sum = carry;
            if (i >= 0) {
                sum += a[i--] - '0';
            }
            if (j >= 0) {
                sum += b[j--] - '0'; 
            }
            carry = sum / 2;
            res.push_back((sum % 2) + '0');
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
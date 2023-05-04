class Solution {
public:
    string predictPartyVictory(string senate) {
        queue<int> qr, qd;
        int n = senate.length();
        for (int i = 0; i < n; i++) {
            (senate[i] == 'R') ? qr.push(i) : qd.push(i);
        }
        while (!qr.empty() && !qd.empty()) {
            int r = qr.front(), d = qd.front();
            qr.pop(), qd.pop();
            (r < d) ? qr.push(r + n) : qd.push(d + n);
        }
        return (qr.empty()) ? "Dire" : "Radiant";
    }
};
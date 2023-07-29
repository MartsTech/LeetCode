class Solution:
    # O(n) time | O(n) spacec
    def reverseWords(self, s: str) -> str:
        r, res = len(s) - 1, []
        while r >= 0:
            if s[r] == ' ':
                r -= 1
                continue
            l = r - 1
            while l >= 0 and s[l] != ' ':
                l -= 1
            for i in range(l + 1, r + 1):
                res += s[i]
            r = l
            res += ' '
        res.pop() # removes extra space
        return ''.join(res)
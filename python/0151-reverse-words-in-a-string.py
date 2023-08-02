class Solution:
    # O(n) time | O(n) space - where n is the length of s
    def reverseWords(self, s: str) -> str:
        res, r = [], len(s) - 1
        while r >= 0:
            if s[r] == " ":
                r -= 1
                continue
            l = r - 1
            while l >= 0 and s[l] != " ":
                l -= 1
            res.append(s[l + 1: r + 1])
            r = l - 1
        return " ".join(res)
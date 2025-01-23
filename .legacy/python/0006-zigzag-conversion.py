class Solution:
    # O(n) time | O(n) space - where n is the lenght of s
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        res, bigStep = [], 2 * (numRows - 1)
        for r in range(numRows):
            for i in range(r, len(s), bigStep):
                res.append(s[i])
                if r == 0 or r == numRows - 1:
                    continue
                smallStep = bigStep - 2 * r
                if i + smallStep < len(s):
                    res.append(s[i + smallStep])
        return "".join(res)
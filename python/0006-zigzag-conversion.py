class Solution:
    # O(n) time | O(n) space
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        res = []
        bigStep = 2 * (numRows - 1)
        for row in range(numRows):
            for i in range(row, len(s), bigStep):
                res.append(s[i])
                if row == 0 or row == numRows - 1:
                    continue
                smallStep = bigStep - 2 * row
                if i + smallStep < len(s):
                    res.append(s[i + smallStep])
        return ''.join(res)
class Solution:
    # O(n) time | O(n) space
    def isValid(self, s: str) -> bool:
        stack = []
        values = {')':'(','}':'{',']':'['}
        for c in s:
            if c not in values:
                stack.append(c)
                continue
            if not stack or values[c] != stack.pop():
                return False
        return not stack
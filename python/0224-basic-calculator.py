class Solution:
    # O(n) time | O(n) space
    def calculate(self, s: str) -> int:
        res, stack = 0, []
        num, sign = 0, 1
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in ["+","-"]:
                res += num * sign
                num, sign = 0, 1 if c == "+" else -1
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1
            elif c == ")":
                res += num * sign
                res *= stack.pop()
                res += stack.pop()
                num, sign = 0, 1
        res += num * sign
        return res
class Solution:
    # O(n) time | O(n) space
    def decodeString(self, s: str) -> str:
        stack = []
        string = ""
        num = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "[":
                stack.append(string)
                stack.append(num)
                string = ""
                num = 0
            elif c == "]":
                prev_num = stack.pop()
                prev_string = stack.pop()
                string = prev_string + prev_num * string
            else:
                string += c
        return string
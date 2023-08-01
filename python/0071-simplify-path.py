class Solution:
    # O(n) time | O(n) space
    def simplifyPath(self, path: str) -> str:
        stack = []
        values = path.split("/")
        for value in values:
            if value == "" or value == ".":
                continue
            elif value == "..":
                if stack: stack.pop()
            else:
                stack.append(value)
        return "/" + "/".join(stack)
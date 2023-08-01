class Solution:
    # O(n) time | O(n) space
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                a, b = stack.pop(), stack.pop()
                match token:
                    case "+": token = a + b
                    case "-": token = b - a
                    case "*": token = a * b
                    case "/": token = b / a
            stack.append(int(token))
        return stack.pop()
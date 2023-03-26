class Solution:
    # O(n) time | O(n) space
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed = [word[::-1] for word in words]
        return " ".join(reversed)
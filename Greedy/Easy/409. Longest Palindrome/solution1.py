class Solution:
    # O(n) time | O(n) space
    def longestPalindrome(self, s: str) -> int:
        result = 0
        cache = {}

        for char in s:
            if char in cache and cache[char] == 1:
                result += 2
                cache[char] = 0
            else:
                cache[char] = 1

        if len(s) - result > 0:
            result += 1

        return result
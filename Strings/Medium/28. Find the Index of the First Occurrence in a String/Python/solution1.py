class Solution:
    # O((n-m)*m) time | O(1) space
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        i = 0
        while i <= len(haystack) - len(needle):
            j = 0
            while j < len(needle) and haystack[i+j] == needle[j]:
                j += 1
            if j == len(needle):
                return i
            i += 1
        return -1

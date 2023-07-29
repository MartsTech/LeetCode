class Solution:
    # O((n-m+1)*m) time | O(1) space
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        for i in range(n - m + 1):
            for j in range(m):
                if haystack[i + j] != needle[j]:
                    break
                if j == m - 1:
                    return i
        return -1 
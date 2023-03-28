class Solution:
    # O(n) time | O(n) space
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        longest = 0
        start = 0
        for end, c in enumerate(s):
            if c in seen and seen[c] >= start:
                start = seen[c] + 1
            seen[c] = end
            longest = max(end - start + 1, longest)
        return longest
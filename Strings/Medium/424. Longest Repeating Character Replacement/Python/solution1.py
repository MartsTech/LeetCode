class Solution:
    # O(n) time | O(1) space
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        right = 0
        max_count = 0
        max_len = 0
        while right < len(s):
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_count = max(max_count, freq[s[right]])
            if right - left + 1 - max_count > k:
                freq[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len
class Solution:
    # O(n) time | O(1) space
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        freq_p = {}
        freq_s = {}
        res = []
        left = 0
        right = len(p) - 1
        for c in p:
            freq_p[c] = freq_p.get(c, 0) + 1
        for i in range(left, right):
            freq_s[s[i]] = freq_s.get(s[i], 0) + 1
        while right < len(s):
            freq_s[s[right]] = freq_s.get(s[right], 0) + 1
            if freq_p == freq_s:
                res.append(left)
            freq_s[s[left]] -= 1
            if freq_s[s[left]] == 0:
                del freq_s[s[left]]
            left += 1
            right += 1
        return res

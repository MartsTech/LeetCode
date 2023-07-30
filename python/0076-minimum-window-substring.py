class Solution:
    # O(m) time | O(n) space - where m is len of s and n is len of t
    def minWindow(self, s: str, t: str) -> str:
        res, res_len = [-1, -1], float('inf')
        s_counter, t_counter = Counter(), Counter(t)
        l = r = 0
        target = len(t)
        while r < len(s):
            if s[r] in t_counter:
                s_counter[s[r]] += 1
                if s_counter[s[r]] <= t_counter[s[r]]:
                    target -= 1
            while target == 0:
                if r - l + 1 < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                if s[l] in s_counter:
                    s_counter[s[l]] -= 1
                    if s_counter[s[l]] < t_counter[s[l]]:
                        target += 1
                l += 1
            r += 1
        return s[res[0]: res[1] + 1] if res_len != float('inf') else ""
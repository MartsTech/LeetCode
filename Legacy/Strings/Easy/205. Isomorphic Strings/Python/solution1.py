class Solution:
    # O(n) time | O(k) space
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_cache = {}
        t_cache = {}
        for (s_value, t_value) in zip(s, t):
            if s_value in s_cache and s_cache[s_value] != t_value:
                    return False
            if t_value in t_cache and t_cache[t_value] != s_value:
                    return False
            s_cache[s_value] = t_value
            t_cache[t_value] = s_value
        return True
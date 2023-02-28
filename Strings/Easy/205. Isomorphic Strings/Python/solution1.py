class Solution:
    # O(n) time | O(n) space
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_cache = {}
        t_cache = {}
        for (s_value, t_value) in zip(s, t):
            if s_value in s_cache:
                if s_cache[s_value] != t_value:
                    return False
            else:
                s_cache[s_value] = t_value
            if t_value in t_cache:
                if t_cache[t_value] != s_value:
                    return False
            else:
                t_cache[t_value] = s_value
        return True


class Solution:
    # O(n) time | O(n) space
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        freq = defaultdict(int)
        for i in range(len(s)):
            freq[s[i]] += 1
            freq[t[i]] -= 1
        for f in freq.values():
            if f != 0: 
                return False
        return True
        
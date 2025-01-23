class Solution:
    # O(n) time | O(n) space
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = defaultdict(int)
        for i in range(len(s)):
            hashmap[s[i]] += 1
            hashmap[t[i]] -= 1
            if hashmap[s[i]] == 0:
                del hashmap[s[i]]
            if hashmap[t[i]] == 0:
                del hashmap[t[i]]
        return not hashmap
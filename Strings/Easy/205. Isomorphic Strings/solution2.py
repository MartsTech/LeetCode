class Solution:
    # O(n) time | O(n) space
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.isIsomorphicHelper(s) == self.isIsomorphicHelper(t)

    def isIsomorphicHelper(self, s: str) -> str:
        cache = {}
        result = []
        for idx, value in enumerate(s):
            if value not in cache:
                cache[value] = idx
            result.append(str(cache[value]))
        return " ".join(result)
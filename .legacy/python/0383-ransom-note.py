class Solution:
    # O(n + m) time | O(n) space
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        counter = Counter(ransomNote)
        for c in magazine:
            if c not in counter:
                continue
            counter[c] -= 1
            if counter[c] == 0:
                del counter[c]
            if not counter:
                return True
        return False
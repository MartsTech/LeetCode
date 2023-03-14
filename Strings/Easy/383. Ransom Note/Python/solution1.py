class Solution:
    # O(m+n) time | O(m) space
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_table = {}
        for c in magazine:
            hash_table[c] = hash_table.get(c, 0) + 1
        for c in ransomNote:
            if c in hash_table and hash_table[c] > 0:
                hash_table[c] -= 1
                continue
            return False
        return True
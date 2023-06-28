class Solution:
    # O(n * m * log m) time | O(n) space - where n is the length of string `s` and m is the length of string `p`
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        word = sorted(p)
        count = len(word)
        for end in range(count - 1, len(s) + 1):
            start = end - count
            if word == sorted(s[start:end]):
                res.append(start)
        return res
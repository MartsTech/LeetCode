class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        idx, count = 1, len(words)
        while idx < count:
            if self.isAnagram(words[idx - 1], words[idx]):
                words.pop(idx)
                count -= 1
            else:
                idx += 1
        return words

    def isAnagram(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        freq = defaultdict(int)
        for i in range(len(word1)):
            freq[word1[i]] += 1
            freq[word2[i]] -= 1
        for f in freq.values():
            if f != 0:
                return False
        return True
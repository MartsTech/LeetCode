class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        idx, count = 1, len(words)
        while idx < count:
            if sorted(words[idx - 1]) == sorted(words[idx]):
                words.pop(idx)
                count -= 1
            else:
                idx += 1
        return words
class Solution:
    # O(n * m) time | O(m) space - where n is the len of s and m the len of words
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res, counter = [], Counter(words)
        word_len, total_len = len(words[0]), len(words[0]) * len(words)
        for i in range(len(s) - total_len + 1):
            j, counts = 0, {}
            while j < total_len:
                word = s[i + j: i + j + word_len]
                if word not in counter:
                    break
                counts[word] = counts.get(word, 0) + 1
                if counts[word] > counter[word]:
                    break
                j += word_len
                if j == total_len:
                    res.append(i)
        return res
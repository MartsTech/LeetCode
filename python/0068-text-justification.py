class Solution:
    # O(n) time | O(n) space - where n is the length of words
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, idx = [], 0
        while idx < len(words):
            line, length = self.getWords(idx, words, maxWidth)
            idx += len(line)
            res.append(self.buildLine(idx, line, length, words, maxWidth))
        return res

    # O(n) time | O(n) space
    def getWords(self, idx: int, words: List[int], maxWidth: int) -> Tuple[List[int], int]:
        line, length = [], 0
        while idx < len(words) and length + len(words[idx]) <= maxWidth:
            line.append(words[idx])
            length += len(words[idx]) + 1
            idx += 1
        lenght -= 1
        return (line, length)

    # O(n) time | O(1) space
    def buildLine(self, idx: int, line: List[int], length: int, words: List[int], maxWidth: int) -> str:
        spaces = maxWidth - length
        if len(line) == 1 or idx == len(words):
            return " ".join(line) + " " * spaces
        words_count = len(line) - 1
        spaces_per_word = spaces // words_count
        for i in range(words_count):
            line[i] += " " * spaces_per_word
        extra_spaces = spaces % words_count
        for i in range(extra_spaces):
            line[i] += " "
        return " ".join(line)
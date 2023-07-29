class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, idx = [], 0
        while idx < len(words):
            line, length = self.get_words(idx, words, maxWidth)
            idx += len(line)
            res.append(self.create_line(line, length, idx, words, maxWidth))
        return res

    def get_words(self, idx: int, words: List[str], maxWidth: int) -> Tuple[List[str], int]:
        line, length = [], 0
        while idx < len(words) and length + len(words[idx]) <= maxWidth:
            line.append(words[idx])
            length += len(words[idx]) + 1
            idx += 1
        length -= 1
        return (line, length)

    def create_line(self, line: List[str], length: int, idx: int, words: List[str], maxWidth: int) -> str:
        spaces = maxWidth - length
        if len(line) == 1 or idx == len(words):
            return ' '.join(line) + ' ' * spaces
        word_count = len(line) - 1
        spaces_per_word = spaces // word_count
        extra_space = spaces % word_count
        for i in range(extra_space):
            line[i] += ' '
        for i in range(word_count):
            line[i] += ' ' * spaces_per_word
        return ' '.join(line)
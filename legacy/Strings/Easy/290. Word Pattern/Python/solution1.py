class Solution:
    # O(n) time | O(n) space
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        letter_to_word = {}
        word_to_letter = {}

        for letter, word in zip(pattern, words):
            if letter in letter_to_word and letter_to_word[letter] != word:
                return False
            if word in word_to_letter and word_to_letter[word] != letter:
                return False
            letter_to_word[letter] = word
            word_to_letter[word] = letter

        return True
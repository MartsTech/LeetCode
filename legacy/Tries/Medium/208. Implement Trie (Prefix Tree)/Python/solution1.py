# 0(n*m) space - where n is the number of words and m is the lenght of the longest word
class Trie:

    def __init__(self):
        self.root = TrieNode()

    # O(m) time - where m is the lenght of the word
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.isWord = True
        
    # O(m) time - where m is the lenght of the word
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if node.children[idx] is None:
                return False
            node = node.children[idx]
        return node.isWord
        
    # O(m) time - where m is the lenght of the prefix
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            idx = ord(char) - ord('a')
            if node.children[idx] is None:
                return False
            node = node.children[idx]
        return True

class TrieNode:

    def __init__(self):
        self.isWord = False
        self.children = [None] * 26
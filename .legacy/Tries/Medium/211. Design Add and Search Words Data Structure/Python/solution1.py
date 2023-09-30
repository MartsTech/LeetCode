class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    # O(n) time | O(n) space - where n is the lenght of the word
    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    # O(m * k) | O(m) space - where m is the lenght of the word and k is the number of words in the trie
    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, idx: int) -> bool:
            if idx == len(word):
                return node.is_word
            if word[idx] == '.':
                for child in node.children.values():
                    if dfs(child, idx + 1):
                        return True
            if word[idx] in node.children:
                return dfs(node.children[word[idx]], idx + 1)
            return False

        return dfs(self.root, 0)
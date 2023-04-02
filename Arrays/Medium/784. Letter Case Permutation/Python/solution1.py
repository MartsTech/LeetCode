class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        self.backtrack("", 0, s, result)
        return result

    def backtrack(self, current: int, index: int, s: str, result: List[str]) -> None:
        if index == len(s):
            result.append(current)
            return
        char = s[index]
        if char.isalpha():
            self.backtrack(current + char.lower(), index + 1, s, result)
            self.backtrack(current + char.upper(), index + 1, s, result)
        else:
            self.backtrack(current + char, index + 1, s, result)
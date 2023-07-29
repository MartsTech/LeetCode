class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.backtrack(1, k, n, [], res)
        return res

    def backtrack(self, start: int, k: int, n: int, curr: List[int], res: List[List[int]]) -> None:
        if k == 0:
            res.append(curr[:])
            return
        for i in range(start, n + 1):
            curr.append(i)
            self.backtrack(i + 1, k - 1, n, curr, res)
            curr.pop()
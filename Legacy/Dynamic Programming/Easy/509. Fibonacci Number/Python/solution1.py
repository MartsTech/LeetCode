class Solution:
    # O(n) time | O(n) space
    def fib(self, n: int, memoize={0: 0, 1: 1}) -> int:
        if n not in memoize:
            memoize[n] = self.fib(n - 1, memoize) + self.fib(n - 2, memoize)
        return memoize[n]

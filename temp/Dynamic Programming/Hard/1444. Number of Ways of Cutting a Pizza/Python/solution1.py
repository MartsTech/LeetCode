class Solution:
    # O(k * n * m * (n+m)) time | O(n * m) space
    def ways(self, pizza: List[str], k: int) -> int:
        rows, cols = len(pizza), len(pizza[0])
        apples = [[0] * (cols + 1) for row in range(rows + 1)]
        for row in reversed(range(rows)):
            for col in reversed(range(cols)):
                apples[row][col] = ((pizza[row][col] == 'A') 
                                    + apples[row+ 1][col] 
                                    + apples[row][col + 1] 
                                    - apples[row + 1][col + 1])
        f = [[int(apples[row][col] > 0) for col in range(cols)] for row in range(rows)]
        mod = 1000000007
        for remain in range(1, k):
            g = [[0 for col in range(cols)] for row in range(rows)]
            for row in range(rows):
                for col in range(cols):
                    for r in range(row + 1, rows):
                        if apples[row][col] - apples[r][col] > 0:
                            g[row][col] += f[r][col]
                    for c in range(col + 1, cols):
                        if apples[row][col] - apples[row][c] > 0:
                            g[row][col] += f[row][c]
                    g[row][col] %= mod
            f = g
        return f[0][0]
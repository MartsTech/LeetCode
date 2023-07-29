class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        n = len(mat)
        for i in range(n):
            sum += mat[i][i]
            sum += mat[n - i - 1][i]
        if n % 2 != 0:
            sum -= mat[n // 2][n // 2]
        return sum
class Solution:
    # O(m*n) time | O(1) space
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] > 0:
                    top = mat[row - 1][col] if row > 0 else float("inf")
                    left = mat[row][col - 1] if col > 0 else float("inf")
                    mat[row][col] = min(top, left) + 1
        for row in reversed(range(rows)):
            for col in reversed(range(cols)):
                if mat[row][col] > 0:
                    bottom = mat[row + 1][col] if row < rows - 1 else float("inf")
                    right = mat[row][col + 1] if col < cols - 1 else float("inf")
                    mat[row][col] = min(mat[row][col], bottom + 1, right + 1)
        return mat
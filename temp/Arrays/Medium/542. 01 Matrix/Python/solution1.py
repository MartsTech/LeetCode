class Solution:
    # O(n*m) time | O(n+m) space
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    queue.append((row, col))
                else:
                    mat[row][col] = -1
        while queue:
            row, col = queue.popleft()
            distance = mat[row][col] + 1
            for r, c in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
                if r < 0 or r >= len(mat) or c < 0 or c >= len(mat[0]) or mat[r][c] != -1:
                    continue
                mat[r][c] = distance
                queue.append((r, c))
        return mat
                    
class Solution:
    # O(m * n) time | O(1) space
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        for r in range(m):
            for c in range(n):
                x = self.count_neighbours(board, r, c)
                if board[r][c] == 0 and x == 3:
                    board[r][c] = 2
                elif board[r][c] == 1 and x not in [2, 3]:
                    board[r][c] = 3
        for r in range(m):
            for c in range(n):
                if board[r][c] == 2:
                    board[r][c] = 1
                elif board[r][c] == 3:
                    board[r][c] = 0
    
    def count_neighbours(self, board: List[List[int]], r: int, c: int) -> int:
        res = 0
        m, n = len(board), len(board[0])
        for dr in range(r - 1, r + 2):
            for dc in range(c - 1, c + 2):
                if dr == r and dc == c:
                    continue
                if dr < 0 or dc < 0 or dr >= m or dc >= n:
                    continue
                if board[dr][dc] in [1, 3]:
                    res += 1
        return res
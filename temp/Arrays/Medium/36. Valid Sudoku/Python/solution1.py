class Solution:
    # O(n^2) time | O(n) space
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            seen = set()
            for cell in row:
                if cell != '.' and cell in seen:
                    return False
                seen.add(cell)
        # Check columns
        for col in range(len(board[0])):
            seen = set()
            for row in range(len(board[0])):
                cell = board[row][col]
                if cell != '.' and cell in seen:
                    return False
                seen.add(cell)
        # Check sub-boxes
        for row_start in range(0, len(board), 3):
            for col_start in range(0, len(board[0]), 3):
                seen = set()
                for row in range(row_start, row_start+3):
                    for col in range(col_start, col_start+3):
                        cell = board[row][col]
                        if cell != '.' and cell in seen:
                            return False
                        seen.add(cell)
        return True
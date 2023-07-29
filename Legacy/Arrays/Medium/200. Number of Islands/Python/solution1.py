class Solution:
    # O(m*n) time | O(m*n) space
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    self.dfs(grid, row, col)
                    result += 1
        return result

    def dfs(self, grid: List[List[str]], row: int, col: int):
        if row < 0 or row == len(grid) or col < 0 or col == len(grid[0]):
            return

        if grid[row][col] != '1':
            return

        grid[row][col] = 'V'

        self.dfs(grid, row + 1, col)
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row, col + 1)
        self.dfs(grid, row, col - 1)

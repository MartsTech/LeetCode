class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    closed = self.dfs(grid, row, col)
                    if closed:
                        count += 1
        return count

    def dfs(self, grid: List[List[int]], row: int, col: int) -> bool:
        grid[row][col] = 2
        closed = True
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x, y = row + dx, col + dy
            if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]):
                if grid[x][y] == 0:
                    closed = self.dfs(grid, x, y) and closed
            else:
                closed = False
        return closed


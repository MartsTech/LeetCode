class Solution:
    # O(m*n) time | O(m*n) space
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    area = self.dfs(grid, row, col)
                    result = max(area, result)
        return result      

    def dfs(self, grid: List[List[int]], row: int, col: int) -> int:
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
            return 0
        grid[row][col] = 0
        area = 1
        area += self.dfs(grid, row + 1, col)
        area += self.dfs(grid, row - 1, col)
        area += self.dfs(grid, row, col + 1)
        area += self.dfs(grid, row, col - 1)
        return area
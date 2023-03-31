class Solution:
    # O(m*n) time | O(m*n) space
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        minutes = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                    grid[row][col] = -2
        while queue:
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()
                for row, col in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != 1:
                        continue
                    queue.append((row, col))
                    grid[row][col] = -2
            if queue:
                minutes += 1
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
        return minutes

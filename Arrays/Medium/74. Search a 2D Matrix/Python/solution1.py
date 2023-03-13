class Solution:
    # O(log(m*n)) time | O(1) space
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) * len(matrix[0])
        while left < right:
            middle = (left + right) // 2
            row = middle // len(matrix[0])
            col = middle - row * len(matrix[0])
            val = matrix[row][col]
            if val > target:
                right = middle
            elif val < target:
                left = middle + 1
            else:
                return True
        return False
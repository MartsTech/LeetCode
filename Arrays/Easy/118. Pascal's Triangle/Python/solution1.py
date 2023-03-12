class Solution:
    # O(numRows^2) time | O(numRows^2) space
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        else:
            result = [[1]]
            for i in range(1, numRows):
                prev = result[-1]
                left = [0] + prev
                right = prev + [0]
                curr = [left[j] + right[j] for j in range(i+1)]
                result.append(curr)
            return result
class Solution:
    # O(n) time | O(n) space
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        visited = {}
        for idx, num in enumerate(numbers):
            match = target - num
            if match in visited:
                return [visited[match], idx + 1]
            visited[num] = idx + 1
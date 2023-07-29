class Solution:
    # O(n*log(n)) time | O(1) space
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        total = 0
        result = 0
        for i in reversed(range(len(satisfaction))):
            if satisfaction[i] >= -total:
                total += satisfaction[i]
                result += total
            else:
                break
        return result
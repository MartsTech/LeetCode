class Solution:
    # O(n) time | O(1) space
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        res = 0
        for val in citations:
            if val > res:
                res += 1
            else:
                break
        return res
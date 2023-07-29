class Solution:
    # O(nlogn) time | O(n) space
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones: 
            heappush(max_heap, -stone)
        while len(max_heap) > 1:
            x = -heappop(max_heap)
            y = -heappop(max_heap)
            if x > y:
                heappush(max_heap, -(x - y))
            elif x < y:
                heappush(max_heap, -(y - x))
        return -heappop(max_heap) if len(max_heap) > 0 else 0
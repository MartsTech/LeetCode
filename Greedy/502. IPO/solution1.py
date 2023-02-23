class Solution:
    # O(nlogn) time } O(n) space
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        n = len(projects)
        queue = []
        priority = 0
        for idx in range(k):
            while priority < n and projects[priority][0] <= w:
                heappush(queue, -projects[priority][1])
                priority += 1
            if not queue:
                break
            w += -heappop(queue)
        return w
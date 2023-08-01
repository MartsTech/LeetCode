class Solution:
    # O(n*log(n)) time | O(1) space
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda i: i[1])
        res, end = 1, points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > end:
                end = points[i][1]
                res += 1 
        return res
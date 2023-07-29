class Solution:
    # O(nlog(m)) time | O(1) space
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        min_time = 0
        max_time = max(time) * totalTrips
        while min_time < max_time:
            mid_time = (min_time + max_time) // 2
            num_trips = 0
            for t in time:
                num_trips += mid_time // t
                if num_trips >= totalTrips:
                    break
            if num_trips >= totalTrips:
                max_time = mid_time
            else:
                min_time = mid_time + 1
        return min_time
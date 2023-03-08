class Solution:
    # O(nlogm) time | O(1) space  
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2
            time = 0
            for pile in piles:
                time += (pile + mid - 1) // mid
            if time <= h:
                right = mid
            else:
                left = mid + 1
        return left
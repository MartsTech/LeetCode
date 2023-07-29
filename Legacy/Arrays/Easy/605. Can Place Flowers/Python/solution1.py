class Solution:
    # O(n) time | O(1) space
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left = flowerbed[max(i - 1, 0)]
                right = flowerbed[min(i + 1, len(flowerbed) - 1)]
                if left == 0 and right == 0:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        break
        return count >= n
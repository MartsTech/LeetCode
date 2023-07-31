class Solution:
    # O(n) time | O(n) space
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for i, num in enumerate(nums):
            if num not in hashmap:
                hashmap[num] = i
                continue
            if abs(i - hashmap[num]) <= k:
                return True
            hashmap[num] = i
        return False
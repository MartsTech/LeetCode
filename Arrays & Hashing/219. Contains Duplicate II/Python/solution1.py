class Solution:
    # O(n) time | O(n) space
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashtable = defaultdict(int)
        for idx, num in enumerate(nums):
            if num in hashtable and idx - hashtable[num] <= k:
                return True
            hashtable[num] = idx
        return False
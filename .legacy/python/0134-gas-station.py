class Solution:
    # O(n) time | O(1) space
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = curr = 0
        res = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            curr += diff
            if curr < 0:
                curr = 0
                res = i + 1
        return res if total >= 0 else -1
        
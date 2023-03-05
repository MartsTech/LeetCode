class Solution:
    # O(nlogn) time | O(1) space
    def sortArray(self, nums: List[int]) -> List[int]:
        self.buildMaxHeap(nums)
        for end in reversed(range(1, len(nums))):
            self.swap(0, end, nums)
            self.siftDown(0, end - 1, nums)
        return nums

    def buildMaxHeap(self, array: List[int]):
        first = (len(array) - 2) // 2
        for idx in reversed(range(first + 1)):
            self.siftDown(idx, len(array) - 1, array)
        
    def siftDown(self, idx: int, end: int, heap: List[int]):
        first = idx * 2 + 1
        while first <= end:
            second = idx * 2 + 2 if idx * 2 + 2 <= end else -1
            if second > -1 and heap[second] > heap[first]:
                swap = second
            else:
                swap = first
            if heap[swap] > heap[idx]:
                self.swap(idx, swap, heap)
                idx = swap
                first = idx * 2 + 1
            else:
                return

    def swap(self, i: int, j: int, nums: List[int]):
        nums[i], nums[j] = nums[j], nums[i]
        
class Solution:
    # O(m + n) time | O(1) space
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        k = m + n
        while n > 0:
            if m > 0 and nums1[m - 1] > nums2[n - 1]:
                nums1[k - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[k - 1] = nums2[n - 1]
                n -= 1
            k -= 1
        
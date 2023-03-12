# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(nlogk) time | O(k) space
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heappush(heap, (lists[i].val, i, lists[i]))
        dummy = ListNode(0)
        curr = dummy
        while heap:
            val, i, node = heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
            if node.next:
                heappush(heap, (node.next.val, i, node.next))
        return dummy.next
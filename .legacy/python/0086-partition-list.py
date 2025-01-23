class Solution:
    # O(n) time | O(1) space - where n is the length of the linked list
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lhead, rhead = ListNode(), ListNode()
        ltail, rtail = lhead, rhead
        while head:
            if head.val < x:
                ltail.next = head
                ltail = ltail.next
            else:
                rtail.next = head
                rtail = rtail.next
            head = head.next
        ltail.next = rhead.next
        rtail.next = None
        return lhead.next
class Solution:
    # O(r) time | O(1) space - where r is the val of right
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevLeft, curr = dummy, dummy.next
        for _ in range(left - 1):
            prevLeft, curr = curr, curr.next
        prev = None
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next, prev = prev, curr
            curr = temp
        prevLeft.next.next = curr
        prevLeft.next = prev
        return dummy.next
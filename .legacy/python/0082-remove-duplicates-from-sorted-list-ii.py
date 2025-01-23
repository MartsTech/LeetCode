class Solution:
    # O(n) time | O(1) space
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, dummy.next
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            if prev.next != curr:
                prev.next = curr.next
            else:
                prev = curr 
            curr = curr.next
        return dummy.next        
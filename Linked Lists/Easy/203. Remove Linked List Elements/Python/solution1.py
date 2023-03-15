# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(n) time | O(1) space
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            if curr.val == val and prev:
                prev.next = curr.next
            elif curr.val == val and not prev:
                head = head.next
            else:
                prev = curr
            curr = curr.next
        return head
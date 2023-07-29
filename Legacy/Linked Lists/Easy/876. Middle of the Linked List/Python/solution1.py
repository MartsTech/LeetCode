# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(n) time | O(1) space
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        idx = 0
        total = 0
        while head:
            total += 1
            if total % 2 == 1 and total // 2 > idx:
                idx += 1
                node = node.next
            head = head.next
        return node if total % 2 == 1 else node.next
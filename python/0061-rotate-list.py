class Solution:
    # O(n) time | O(1) space - where n is the length of the linked list
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1
        k %= length
        if k == 0: return head
        curr = head
        for _ in range(length - k - 1):
            curr = curr.next
        tail.next = head
        head = curr.next
        curr.next = None
        return head
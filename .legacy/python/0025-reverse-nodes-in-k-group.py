class Solution:
    # O(n) time | O(1) space - where n is the length of the linked list
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            kth = self.getKth(groupPrev, k)
            if not kth: break
            groupNext = kth.next
            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                temp = curr.next
                curr.next, prev = prev, curr
                curr = temp
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        return dummy.next

    # O(k) time | O(1) space - where k is the value of k
    def getKth(self, node: ListNode, k: int) -> Optional[ListNode]:
        while node and k > 0:
            node = node.next
            k -= 1
        return node
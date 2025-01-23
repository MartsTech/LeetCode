class Solution:
    # O(n) time | O(n) space
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {None: None}
        curr = head
        while curr:
            copy = Node(curr.val)
            hashmap[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            hashmap[curr].next = hashmap[curr.next]
            hashmap[curr].random = hashmap[curr.random]
            curr = curr.next
        return hashmap[head]
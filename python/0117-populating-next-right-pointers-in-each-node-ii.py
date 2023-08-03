class Solution:
    # O(n) time | O(d) space
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        queue = deque([root])
        while queue:
            prev = Node()
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node: continue
                prev.next = node
                prev = node
                queue.append(node.left)
                queue.append(node.right)
            prev.next = None
        return root
class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap, self.cache = capacity, {}
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    # O(1) time
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    # O(1) time
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            node = self.head.next
            self.remove(node)
            del self.cache[node.key]

    # O(1) time
    def remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    # O(1) time
    def insert(self, node: Node) -> None:
        node.prev, node.next = self.tail.prev, self.tail
        self.tail.prev.next = self.tail.prev = node
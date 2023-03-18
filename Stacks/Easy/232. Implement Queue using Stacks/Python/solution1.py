class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    # O(1) time | O(1) space
    def push(self, x: int) -> None:
        self.s1.append(x)

    # O(n) time | O(n) space
    def pop(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    # O(n) time | O(n) space
    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]
        
    # O(1) time | O(1) space
    def empty(self) -> bool:
        return not self.s1 and not self.s2
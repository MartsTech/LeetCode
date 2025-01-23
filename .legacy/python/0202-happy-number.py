class Solution:
    # O(n) time | O(1) space
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.getNext(n)
        while slow != fast and fast != 1:
            slow = self.getNext(slow)
            fast = self.getNext(self.getNext(fast))
        return fast == 1
        
    def getNext(self, n: int) -> int:
        res = 0
        while n > 0:
            num = n % 10
            n //= 10
            res += num ** 2
        return res
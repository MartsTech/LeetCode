class Solution:
    # O(n) time | O(1) space
    def intToRoman(self, num: int) -> str:
        values = {1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
        res = ""
        for key, value in reversed(values.items()):
            count = num // key
            res += value * count
            num %= key
            if num == 0:
                break
        return res
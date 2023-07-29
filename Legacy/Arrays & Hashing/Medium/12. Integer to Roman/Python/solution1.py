class Solution:
    values = {1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}

    # O(1) time | O(1) space
    def intToRoman(self, num: int) -> str:
        res = ""
        for val, sym in reversed(self.values.items()):
            if num // val:
                count = num // val
                res += (sym * count)
                num %= val
        return res
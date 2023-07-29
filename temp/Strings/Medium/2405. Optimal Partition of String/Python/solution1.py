class Solution:
    def partitionString(self, s: str) -> int:
        partitions = 1
        chars_bitmask = 0
        for c in s:
            set_bit = 1 << (ord(c) - 97)
            if chars_bitmask & set_bit:
                partitions += 1
                chars_bitmask = 0
            chars_bitmask |= set_bit
        return partitions
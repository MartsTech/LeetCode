class Solution:
    # O(n) time | O(1) space
    def compress(self, chars: List[str]) -> int:
        left = 0
        right = 0
        while right < len(chars):
            count = 1
            while right < len(chars) - 1 and chars[right] == chars[right + 1]:
                count += 1
                right += 1
            chars[left] = chars[right]
            left += 1
            if count > 1:
                for num in str(count):
                    chars[left] = num
                    left += 1
            right += 1
        return left
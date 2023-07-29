class Solution:
    # O(n) time | O(1) space
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        w = len(s1)
        matched = 0
        for i in range(len(s2)):
            if s2[i] in counter:
                counter[s2[i]] -= 1
                if counter[s2[i]] == 0:
                    matched += 1
            if i >= w and s2[i-w] in counter:
                if counter[s2[i-w]] == 0:
                    matched -= 1
                counter[s2[i - len(s1)]] += 1
            if matched == len(counter):
                return True
        return False
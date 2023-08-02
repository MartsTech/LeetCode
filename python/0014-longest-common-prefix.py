class Solution:
    # O(n * m) time | O(1) space - where n is the length of strs and m is the length of the shortest string in strs
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count = 0
        for i in range(len(strs[0])):
            for s in range(1, len(strs)):
                if i == len(strs[s]) or strs[0][i] != strs[s][i]:
                    return strs[0][:count]
            count += 1
        return strs[0][:count]
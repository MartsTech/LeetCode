class Solution:
    # O(min(strs)) time | O(1) space
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in range(1, len(strs)):
                if i == len(strs[s]) or strs[s][i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=min(len(s) for s in strs)
        for j in range(n):
            char = strs[0][j]
            for i in range(1,len(strs)):
                if strs[i][j]!=char:
                    return strs[0][:j]
        return strs[0][:n]

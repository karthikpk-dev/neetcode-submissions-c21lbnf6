class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1)
        n=len(text2)
        memo={}
        def fun(i,j):
            if i>=m or j>=n:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if text1[i]==text2[j]:
                memo[(i,j)]= 1 + fun(i+1,j+1)
            else:
                memo[(i,j)] = max(fun(i,j+1),fun(i+1,j))
            return memo[(i,j)]
        return fun(0,0)
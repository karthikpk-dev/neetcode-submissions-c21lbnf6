class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1)
        n=len(text2)
        memo={}
        dp=[[0] * (n+1) for _ in range(m+1)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if text1[i]==text2[j]:
                    dp[i][j]= 1 + dp[i+1][j+1]
                else:
                    dp[i][j]= max(dp[i][j+1],dp[i+1][j])
        return dp[0][0]
        # def fun(i,j):
        #     if i>=m or j>=n:
        #         return 0
        #     if (i,j) in memo:
        #         return memo[(i,j)]
        #     if text1[i]==text2[j]:
        #         memo[(i,j)]= 1 + fun(i+1,j+1)
        #     else:
        #         memo[(i,j)] = max(fun(i,j+1),fun(i+1,j))
        #     return memo[(i,j)]
        # return fun(0,0)
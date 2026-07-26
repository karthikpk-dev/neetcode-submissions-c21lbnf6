class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[0]* (n+1) for _ in range(m+1)]

        dp[m-1][n-1]=1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i == m - 1 and j == n - 1:
                    continue
                dp[i][j]= dp[i+1][j] + dp[i][j+1]
        return dp[0][0]
        # memo={}
        # def fun(i,j):
        #     if i>=m or j>=n:
        #         return 0
        #     if i==m-1 and j==n-1:
        #         return 1
        #     if (i,j) in memo:
        #         return memo[(i,j)]

        #     d = fun(i+1,j)
        #     r = fun(i,j+1)
        #     memo[(i,j)]= d + r
        #     return memo[(i,j)]
        # return fun(0,0)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n=len(obstacleGrid) , len(obstacleGrid[0])
        dp=[[0]*(n+1) for _ in range(m+1)]
        if obstacleGrid[m - 1][n - 1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        dp[m-1][n-1]=1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i==m-1 and j==n-1:
                    continue
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                else:
                    dp[i][j]=dp[i+1][j]+dp[i][j+1]
        return dp[0][0]

        # def fun(i,j):
            
        #     if i>=m or j>=n or obstacleGrid[i][j]==1:
        #         return 0
        #     if i==m-1 and j==n-1:
        #         return 1
        #     if (i,j) in memo:
        #         return memo[(i,j)]
        #     bottom = fun(i+1,j)
        #     right= fun(i,j+1)
        #     memo[(i,j)]= bottom + right
        #     return memo[(i,j)]
        # return fun(0,0)
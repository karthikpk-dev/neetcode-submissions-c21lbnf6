class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n=len(obstacleGrid) , len(obstacleGrid[0])
        memo={}
        def fun(i,j):
            
            if i>=m or j>=n or obstacleGrid[i][j]==1:
                return 0
            if i==m-1 and j==n-1:
                return 1
            if (i,j) in memo:
                return memo[(i,j)]
            bottom = fun(i+1,j)
            right= fun(i,j+1)
            memo[(i,j)]= bottom + right
            return memo[(i,j)]
        return fun(0,0)
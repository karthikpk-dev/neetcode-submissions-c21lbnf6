from math import inf
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        memo={}
        def fun(i,j):
            if i>=m or j>=n:
                return inf
            if i==m-1 and j==n-1:
                return grid[i][j]
            if (i,j) in memo:
                return memo[(i,j)]
            bottom = fun(i+1,j) + grid[i][j]
            right = fun(i,j+1) + grid[i][j]
            memo[(i,j)]=min(bottom,right)
            return memo[(i,j)]
        return fun(0,0)
            
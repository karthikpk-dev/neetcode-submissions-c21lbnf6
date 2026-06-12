class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        visited=[[False for _ in range(n) ] for _ in range(m)]
        res=0
        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n or visited[i][j] or grid[i][j]==0:
                return 0
            visited[i][j]=True
            return 1+ dfs(i+1,j) + dfs(i,j+1) + dfs(i-1,j) +dfs(i,j-1)
 


        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j]==1:
                    res= max(res,dfs(i,j))
        return res
            
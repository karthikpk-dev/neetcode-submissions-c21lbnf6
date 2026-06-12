class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        cnt=0
        visited = [[False for _ in range(n)] for _ in range(m)]

        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n or grid[i][j]=="0" or visited[i][j]:
                return
            visited[i][j]=True
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)

        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and visited[i][j]==False:
                    dfs(i,j)
                    cnt+=1
        return cnt
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m,n=len(grid),len(grid[0])
        q=deque()
        INF=2147483647
        visit=set()

        def addToCell(r,c):
            if r>=m or c>=n or (min(r,c)) < 0 or (r,c) in visit or grid[r][c]==-1:
                return
            visit.add((r,c))
            q.append((r,c))
            


        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    q.append((i,j))
                    visit.add((i,j))

        dist=0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c]=dist
                addToCell(r+1,c)
                addToCell(r,c+1)
                addToCell(r-1,c)
                addToCell(r,c-1)
            dist+=1
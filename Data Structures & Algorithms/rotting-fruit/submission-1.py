class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        visit=set()
        q=deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
                    visit.add((i,j))
        def addToQ(r,c):
            if min(r,c)< 0 or r>=m or c>=n or (r,c) in visit or grid[r][c]==0:
                return
            grid[r][c]=2
            q.append((r,c))
            visit.add((r,c))


        dist=0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                addToQ(r+1,c)
                addToQ(r,c+1)
                addToQ(r-1,c)
                addToQ(r,c-1)
            if q:
                dist+=1

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return -1
        return dist
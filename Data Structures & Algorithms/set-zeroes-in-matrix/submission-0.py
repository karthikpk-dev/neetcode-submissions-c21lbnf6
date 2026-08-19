class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        m,n=len(matrix),len(matrix[0])
        r,c=[False]*m , [False]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    r[i]=True
                    c[j]=True
        for i in range(m):
            for j in range(n):
                if r[i] is True or c[j] is True:
                    matrix[i][j]=0


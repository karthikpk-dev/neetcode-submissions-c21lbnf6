class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m=n=len(matrix)
        res=[[0]*m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                res[i][j]=matrix[m-1-j][i]
        matrix[:]=res
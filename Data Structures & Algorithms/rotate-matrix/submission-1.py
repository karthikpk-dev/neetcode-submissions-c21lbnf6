class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m=n=len(matrix)
        

        i=0
        while i<m//2:
            for j in range(n):
                matrix[i][j],matrix[m-1-i][j]=matrix[m-1-i][j],matrix[i][j]
            i+=1
        for i in range(m):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                if i >0 and j>0:
                    self.matrix[i][j]= matrix[i][j] + self.matrix[i-1][j] + self.matrix[i][j-1]-self.matrix[i-1][j-1]
                elif i > 0:
                    self.matrix[i][j]= matrix[i][j]+ self.matrix[i-1][j]
                elif j>0:
                    self.matrix[i][j]= matrix[i][j] + self.matrix[i][j-1]
                else:
                    self.matrix[i][j]=matrix[i][j]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.matrix[row2][col2]

        top = self.matrix[row1-1][col2] if row1 > 0 else 0
        left = self.matrix[row2][col1-1] if col1 > 0 else 0
        overlap = self.matrix[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0

        return total - top - left + overlap

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
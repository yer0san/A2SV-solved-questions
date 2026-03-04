class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.mat = []
        mat0 = [0]*(len(matrix[0])+1)
        self.mat.append(mat0)
        for i in range(len(matrix)):
            mat1 = [0]
            for j in range(len(matrix[0])):
                ad = matrix[i][j]-self.mat[i][j]+mat1[-1]+self.mat[i][j+1]
                mat1.append(ad)
            self.mat.append(mat1)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.mat[row2+1][col2+1] - self.mat[row2+1][col1] - self.mat[row1][col2+1] + self.mat[row1][col1]
        

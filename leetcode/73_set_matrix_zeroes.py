class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroes = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroes.append((i, j))
        
        for z in zeroes:
            
            for j in range(len(matrix[0])):
                matrix[z[0]][j] = 0
            for i in range(len(matrix)):
                matrix[i][z[1]] = 0

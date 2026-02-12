class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        x = y = 0
        for i in range(n//2):
            for j in range(n - (i*2) - 1):
                change = 0
                for k in range(3):
                    if change == 0:
                        matrix[x][y], matrix[y][n-i-1] = matrix[y][n-i-1], matrix[x][y]
                    elif change == 1:
                        matrix[x][y], matrix[n-i-1][n-y-1] = matrix[n-i-1][n-y-1], matrix[x][y]
                    elif change == 2:
                        matrix[x][y], matrix[n-y-1][i] = matrix[n-y-1][i], matrix[x][y]
                    change += 1
                y += 1
            
            x, y = x+1, x+1

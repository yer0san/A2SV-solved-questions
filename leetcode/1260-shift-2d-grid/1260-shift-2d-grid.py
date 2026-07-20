class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # easy to bruteforce 100 * 50 * 50
        m = len(grid)
        n = len(grid[0])
        for _ in range(k):
            cur = grid[0][0]
            for i in range(m):
                for j in range(n):
                    if j == n-1 and i == m-1:
                        grid[0][0] = cur
                        continue
                    if j == n-1:
                        temp = grid[i+1][0]
                        grid[i+1][0] = cur
                        cur = temp
                        continue
                    temp = grid[i][j+1]
                    grid[i][j+1] = cur
                    cur = temp
        return grid

# matrices suck
        

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        n = len(mat)
        
        prev = [lis[:] for lis in mat]
        for _ in range(3):
            rotated = []
            for j in range(n):
                ith = []
                for i in range(n):
                    ith.append(prev[i][j])
                ith.reverse()
                rotated.append(ith)
            if rotated == target:
                return True
            prev = [lis[:] for lis in rotated]
        return False

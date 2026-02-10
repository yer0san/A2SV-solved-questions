class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        seen = set()
        res = []
        right = left = down = up = False
        i = [0, 0]
        res.append(matrix[i[0]][i[1]])
        seen.add((0, 0))
        while True:
            # to the right
            while (i[0], i[1]+1) not in seen and i[1]+1 < len(matrix[0]):
                right = True
                i[1] += 1
                res.append(matrix[i[0]][i[1]])
                seen.add((i[0], i[1]))
    
            # downwards
            while (i[0]+1, i[1]) not in seen and i[0]+1 < len(matrix):
                left = True
                i[0] += 1
                res.append(matrix[i[0]][i[1]])
                seen.add((i[0], i[1]))

            # leftwards
            while (i[0], i[1]-1) not in seen and i[1]-1 >= 0:
                down = True
                i[1] -= 1
                res.append(matrix[i[0]][i[1]])
                seen.add((i[0], i[1]))
            
            #  upwards
            while (i[0]-1, i[1]) not in seen and i[0]-1 >= 0:
                up = True
                i[0] -= 1
                res.append(matrix[i[0]][i[1]])
                seen.add((i[0], i[1]))
            if right and down and left and up:
                right = down = left = up = False
                continue
            else:
                break
        return res

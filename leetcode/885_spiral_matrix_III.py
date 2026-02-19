class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = [[rStart, cStart]]
        count = 0
        while len(res) < rows*cols:
            count += 1
            # to the  right and down
            i = 0
            while i < count:
                cStart += 1
                if rStart >= 0 and rStart < rows and cStart >= 0 and cStart < cols:
                    res.append([rStart, cStart])
                i += 1
            
            i = 0
            while i < count:
                rStart += 1
                if rStart >= 0 and rStart < rows and cStart >= 0 and cStart < cols:
                    res.append([rStart, cStart])
                i += 1
            
            # to the left and up
            count += 1
            i = 0
            while i < count:
                cStart -= 1
                if rStart >= 0 and rStart < rows and cStart >= 0 and cStart < cols:
                    res.append([rStart, cStart])
                i += 1
            
            i = 0
            while i < count:
                rStart -= 1
                if rStart >= 0 and rStart < rows and cStart >= 0 and cStart < cols:
                    res.append([rStart, cStart])
                i += 1
        
        return res


            
            
            

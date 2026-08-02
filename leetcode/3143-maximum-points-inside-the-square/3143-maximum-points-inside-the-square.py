class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        point_tag = dict()
        for i in range(len(s)):
            point_tag[(points[i][0], points[i][1])] = s[i] # tuple with a character
        
        points.sort(key=lambda x: max(abs(x[0]), abs(x[1])))
        
        res = 0
        count = 0
        prev = 0
        seen = set()

        for x, y in points:
            cur = max(abs(x), abs(y))
            if cur != prev:
                res += count 
                count = 0
                prev = cur
            if point_tag[(x, y)] in seen:
                count = 0
                break
            
            seen.add(point_tag[(x, y)])
            count += 1

        return res + count
# this should work, edge cases?? idts
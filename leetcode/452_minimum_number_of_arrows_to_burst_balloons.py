class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        points.sort()
        res = 1
        minimum = points[0]

        for point in points[1:]:
            if point[0] <= minimum[1]:
                minimum[0], minimum[1] = max(minimum[0], point[0]), min(minimum[1], point[1])
            else:
                res += 1
                minimum = point

        return res

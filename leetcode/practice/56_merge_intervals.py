class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort()
        res = []

        first = intervals[0][0]
        last = intervals[0][1]
        for i in range(1, len(intervals)):
            
            if last < intervals[i][0]:
                res.append([first, last])
                first = intervals[i][0]
            last = max(last, intervals[i][1])
        res.append([first, last])
        return res

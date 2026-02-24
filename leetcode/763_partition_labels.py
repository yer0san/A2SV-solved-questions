class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mapper = defaultdict(list)
        for i, l in enumerate(s):
            mapper[l].append(i) 
        
        m = mapper[s[0]][-1]
        beg = mapper[s[0]][0]
        res = []
        fresh = False
        for i, l in enumerate(s):
            if fresh:
                m = mapper[l][-1]
                beg = mapper[l][0]
                fresh = False
            if i == m:
                res.append(m-beg+1)
                fresh = True
                continue
            m = max(m, mapper[l][-1])
            beg = min(beg, mapper[l][0])
        return res

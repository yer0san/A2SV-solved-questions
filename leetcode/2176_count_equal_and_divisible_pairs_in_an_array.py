class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        mapper = defaultdict(list)
        for i, n in enumerate(nums):
            mapper[n].append(i)
        res = 0
        print(mapper)
        for n in mapper:
            if len(mapper[n]) == 1:
                continue
            for i in range(len(mapper[n])):
                for j in range(i+1, len(mapper[n])):
                    if (mapper[n][i]*mapper[n][j])%k == 0:
                        res += 1
        return res # over-engineered? YES, yes it is. Beautiful? Also yes !

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = 0
        mapper = defaultdict(int)
        mapper[0] = 1
        res = 0

        for num in nums:
            pre += num
            if pre-k in mapper:
                res += mapper[pre-k]
            mapper[pre] += 1
        return res

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pre = 0
        wn = defaultdict(int)
        wn[0] += 1
        res = 0

        for num in nums:
            pre += num
            if pre%k in wn:
                res += wn[pre%k]
            wn[pre%k] += 1
        return res


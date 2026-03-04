class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pre = 0
        m = defaultdict(int)
        m[0] = 1
        res = 0

        for num in nums:
            pre += num
            if pre-goal in m:
                res += m[pre-goal]
            m[pre] += 1
        return res

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cnt0 = 0
        res = 0
        wn = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                cnt0 += 1
            while cnt0 > 1:
                if nums[l] == 0:
                    cnt0 -= 1
                l += 1
            res = max(res, r-l+1)
        return res-1

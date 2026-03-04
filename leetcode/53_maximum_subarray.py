class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = [0]
        all_neg = True
        for num in nums:
            if num > 0:
                all_neg = False
            pre.append(pre[-1]+num)
        if all_neg:
            return max(nums)
        res = 0
        mn = 0
        for num in pre:
            mn = min(mn, num)
            res = max(res, abs(mn-num))
        return res

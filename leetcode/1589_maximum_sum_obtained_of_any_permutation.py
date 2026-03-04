class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        pre_b = [0]*(len(nums)+1)
        
        for l, r in requests:
            pre_b[l] += 1
            pre_b[r+1] -= 1
        
        pre = [0]
        for pr in pre_b:
            pre.append(pre[-1]+pr)

        nums.sort(reverse=True)
        pre.sort(reverse=True)

        res = 0
        for i, num in enumerate(nums):
            res += num*pre[i]
        return res%((10**9)+7)

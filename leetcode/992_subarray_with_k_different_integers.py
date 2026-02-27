class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        c = defaultdict(int)
        res = 0
        l = 0
        for r in range(len(nums)):
            c[nums[r]] += 1
            while len(c) > k:
                c[nums[l]] -= 1
                if c[nums[l]] == 0:
                    del c[nums[l]]
                l += 1
            res += r-l+1
        c = defaultdict(int)
        res2 = 0
        l = 0
        for r in range(len(nums)):
            c[nums[r]] += 1
            while len(c) >= k:
                c[nums[l]] -= 1
                if c[nums[l]] == 0:
                    del c[nums[l]]
                l += 1
            res2 += r-l+1
        
        return res-res2
        

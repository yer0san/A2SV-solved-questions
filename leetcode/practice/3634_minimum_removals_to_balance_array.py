class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        res = float('inf')
        for i, num in enumerate(nums):
            
            if nums[left]*k < num:
                while nums[left]*k < num:
                    left += 1
            res = min(res,len(nums) - (i-left+1))

        return res

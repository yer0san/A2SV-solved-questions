class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        res = nums[0]
        nums = nums[1:]
        m = min(nums)
        res += m
        nums.remove(m)
        return res + min(nums) # yeah it's a bad solution :)

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = sorted(nums)
        res.sort()
        
        d = {}
        for i in range(len(res)-1, -1, -1):
            d[res[i]] = i
        for i in range(len(nums)):
            nums[i] = d[nums[i]]
        return nums

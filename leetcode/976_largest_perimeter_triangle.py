class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort() 
        n = 2
        res = 0
        while n < len(nums):
            a, b, c = nums[n-2], nums[n-1], nums[n]
            if a+b > c and a+c > b and b+c >a:
                res = max(res, a+b+c)
            n += 1
        return res

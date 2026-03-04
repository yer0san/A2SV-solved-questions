class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0]*len(nums)
        
        tot = 1
        zer = False
        for num in nums:
            if num != 0:
                tot *= num
            else:
                zer = True
        
        if zer:
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i] = 0
                else:
                    nums[i] = tot
            return nums
        for i in range(len(nums)):
            nums[i] = tot//nums[i]
        return nums

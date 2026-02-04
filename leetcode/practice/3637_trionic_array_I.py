class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if len(nums) == 3 or nums[1] <= nums[0]:
            return False

        # first phase
        c = 1
        while nums[c] > nums[c-1]:
            c += 1
            if c >= len(nums):
                return False
        # second phase
        while nums[c] < nums[c-1]:
            c += 1
            if c >= len(nums):
                return False
        # third phase
        while nums[c] > nums[c-1]:
            c += 1
            if c >= len(nums):
                return True
        return False

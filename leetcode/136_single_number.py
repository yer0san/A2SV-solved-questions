class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0^nums[0]
        for num in nums[1:]:
            res = res^num
        return res

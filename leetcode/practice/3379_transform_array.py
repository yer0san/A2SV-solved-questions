class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        left = nums[::-1]
        result = [0 for _ in range(len(nums))]
        # positive or 0 ones
        for i, num in enumerate(nums):
            if num >= 0:
                result[i] = nums[(i+num)%len(nums)]
        # negative ones
        for i in range(len(nums)-1, -1, -1):
            if left[i] < 0:
                result[(len(nums)-1) - i] = left[(i+abs(left[i]))%len(nums)]
        return result

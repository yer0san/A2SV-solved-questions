class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        pre = 0
        mn = 0
        for num in nums:
            pre += num
            mn = min(mn, pre)
        
        return abs(mn)+1

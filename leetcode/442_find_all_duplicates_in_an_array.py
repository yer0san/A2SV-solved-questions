class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = set()
        count = Counter(nums)
    
        for num in nums:
            if count[num] == 2:
                res.add(num)
        return list(res)

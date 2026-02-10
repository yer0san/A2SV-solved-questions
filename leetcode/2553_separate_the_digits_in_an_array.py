class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            str_num = str(num)
            for n in str_num:
                res.append(int(n))
        return res

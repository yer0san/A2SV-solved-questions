class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        prev_sum = 0
        res = []

        for num in nums:
            prev_sum += num if num%2==0 else 0

        for num,idx in queries: 
            
            if nums[idx]%2==0:
                prev_sum -= nums[idx]

            nums[idx] += num
            if nums[idx] % 2 == 0:
                prev_sum += nums[idx]
            res.append(prev_sum)
        return res

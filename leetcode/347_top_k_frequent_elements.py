from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        nums.sort(key=lambda x: freq[x], reverse=True)
        seen = set()
        res = []
        for num in nums:
            if num not in seen:
                res.append(num)
                seen.add(num)

        return res[:k]

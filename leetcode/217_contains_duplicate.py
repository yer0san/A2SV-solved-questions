class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        stt = set(nums)
        return len(stt) != len(nums)

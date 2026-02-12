class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        counts = Counter(nums)
        dom = max(counts, key = lambda x : counts[x])
        occ = counts[dom]

        dom_count = 0
        for i in range(len(nums)):
            if nums[i] == dom:
                dom_count += 1

            right_count = occ - dom_count

            if dom_count > (i + 1)//2 and right_count > (n - i-1)//2:
                return i

        return -1

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l = 0
        r = len(people)-1
        people.sort()
        res = 0
        while l <= r:
            if l == r:
                res += 1
                l += 1
                continue
            if people[l]+people[r] <= limit:
                res += 1
                r -= 1
                l += 1
                continue
            r -= 1
            res += 1
        return res

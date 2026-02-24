class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        s = skill[0] + skill[-1]
        l = 0
        r = len(skill)-1
        res = 0
        while l < r:
            if skill[l]+skill[r] == s:
                res += skill[l]*skill[r]
            else:
                return -1
            l += 1
            r -= 1
        return res

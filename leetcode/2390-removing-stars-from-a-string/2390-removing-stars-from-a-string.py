class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        for l in s:
            if res and l == '*':
                res.pop()
            else:
                res.append(l)
        return "".join(res)
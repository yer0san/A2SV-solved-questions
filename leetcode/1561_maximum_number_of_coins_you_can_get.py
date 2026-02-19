class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = 1
        res = 0

        while n < (len(piles)-(len(piles)/3)):
            res += piles[n]
            n += 2
        return res

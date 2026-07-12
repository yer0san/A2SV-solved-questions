class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arrS = sorted(arr)

        seen = {}
        rank = 1
        for num in arrS:
            if num not in seen:
                seen[num] = rank
                rank += 1
        
        res = []
        for num in arr:
            res.append(seen[num])
        
        return res # space complexity went to shits tho hehe


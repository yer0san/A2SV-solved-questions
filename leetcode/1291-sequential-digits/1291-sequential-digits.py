class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        mx = "123456789"
        # two pointers to slice this mf
        l = 0
        r = 1

        res = []
        
        while l < 9:
            while r < 10:
                seg = int(mx[l:r])

                if seg >= low and seg <= high:
                    res.append(seg)
                r += 1
            l += 1
            r = l+1
        res.sort()
        return res


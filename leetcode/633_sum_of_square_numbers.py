class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        check = []
        s = 0
        while True:
            check.append(s**2)
            if s**2 >= c:
                break
            s += 1
        l = 0
        r = len(check)-1
        while l <= r:
            if check[l] + check[r] == c:
                return True
            elif check[l]+check[r] > c:
                r -= 1
            else:
                l += 1
        return False 

class Solution:
    def isHappy(self, n: int) -> bool:
        checker = set()
        while True:
            if n == 1:
                return True
            res = 0
            while n >= 1:
                y = n % 10
                res += y**2
                n //= 10
            if res in checker:
                return False
            checker.add(res)
            n = res

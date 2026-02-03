class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        right = len(x)-1
        for n in x:
            if n != x[right]:
                return False
            right -= 1
        return True

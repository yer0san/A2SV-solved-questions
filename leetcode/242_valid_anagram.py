class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # this is a comment, best practice :)
        return sorted(s) == sorted(t)

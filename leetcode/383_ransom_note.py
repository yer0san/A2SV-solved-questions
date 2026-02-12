class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransoms = Counter(ransomNote)
        mag = Counter(magazine)

        for ransom in ransoms:
            if ransoms[ransom] > mag[ransom]:
                return False
        return True

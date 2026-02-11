class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False
        count1 = Counter(word1)
        count2 = Counter(word2)
        lis1 = list(count1.values())
        lis2 = list(count2.values())
        lis1.sort()
        lis2.sort()
        return lis1 == lis2

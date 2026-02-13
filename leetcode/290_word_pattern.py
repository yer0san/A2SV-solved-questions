class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s = s.split()
        if len(s) != len(pattern):
            return False
        mapper = defaultdict(str)
        seen = set()
        for i,l in enumerate(pattern):
            if l in mapper:
                if s[i] != mapper[l]:
                    return False
            else:
                if s[i] in seen:
                    return False
                mapper[l] = s[i]
                seen.add(s[i])
        return True

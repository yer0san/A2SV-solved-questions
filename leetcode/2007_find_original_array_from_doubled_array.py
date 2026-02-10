class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2 != 0:
            return []

        changed.sort()
        hash = {num:num*2 for num in changed}
        res = []
        seen = set()
        freq = Counter(changed)
        if freq[0]%2 != 0:
            return []

        for key in changed:
            val = hash[key]
            if key in seen or val in seen:
                continue
            if val not in hash:
                return []
            res.append(key)
            freq[key] -= 1
            freq[val] -= 1
            if freq[key] == 0:
                seen.add(key)
            if freq[val] == 0:
                seen.add(val)

        return res if len(res) == len(changed)//2 else [] # well, it barely works lol

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        sorted_s = sorted(freq, key = lambda x: freq[x], reverse=True)

        res = []

        for l in sorted_s:
            for _ in range(freq[l]):
                res.append(l)
        return "".join(res)

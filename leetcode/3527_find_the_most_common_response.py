class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        freq = defaultdict(int)
        for response in responses:
            seen = set()
            for r in response:
                if r not in seen:
                    freq[r] += 1
                    seen.add(r)

        maxxes = []
        max_freq = max(freq.values())
        for resp, f in freq.items():

            if f == max_freq:
                maxxes.append(resp)
        return min(maxxes)

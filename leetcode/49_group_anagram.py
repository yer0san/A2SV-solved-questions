class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_res = defaultdict(list)
        for s in strs:
            sorted_s = sorted(s)
            map_res["".join(sorted_s)].append(s)
        return [val for val in map_res.values()]

            

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        idx = 0
        strs = sorted(strs, key=lambda x: len(x))
        for l in strs[0]:
            for word in strs:
                if word == "":
                    return ""
                if l != word[idx]:
                    return "".join(res)
            res.append(l)
            idx += 1
        return "".join(res)

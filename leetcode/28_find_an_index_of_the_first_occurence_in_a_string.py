class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        stack = []
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                stack.append(i)
        for idx in stack:
            i = idx
            s = 0
            while idx < len(haystack):
                if haystack[idx] != needle[s]:
                    break
                else:
                    s += 1
                if s == len(needle):
                    return i
                idx += 1
        return -1  # did i overengineer it? yes, yes i did. or so i think

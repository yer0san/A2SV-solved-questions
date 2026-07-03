class Solution:
    def letterCombinations(self, digits: str):
        mapp = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        res = []
        def backtrack(st, lis, dig):
            if len(lis) == len(digits):
                res.append("".join(lis[:]))
                return

            for i in range(st, len(digits)):
                for el in mapp[digits[i]]:
                    if el in lis or digits[i] in dig:
                        continue
                    lis.append(el)
                    dig.append(digits[i])
                    backtrack(st+1, lis, dig)
                    lis.pop()
                    dig.pop()
        backtrack(0, [], [])
        return res

sol = Solution()
print(sol.letterCombinations('234'))

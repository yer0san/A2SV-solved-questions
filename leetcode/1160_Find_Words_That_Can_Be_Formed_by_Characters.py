class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        res = 0
        for word in words:
            ch = list(chars)
            dont = False
            for i in range(len(word)):
                if word[i] not in ch:
                    dont = True
                    break
                ch.remove(word[i])
            if not dont:
                res += len(word)

        return res

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq = Counter(s)
        stack = []

        seen = set()

        for c in s:
            freq[c] -= 1

            if c in seen:
                continue


            while stack and c < stack[-1] and freq[stack[-1]] > 0:
                seen.remove(stack.pop())

            stack.append(c)
            seen.add(c)

        return "".join(stack)

# i am s-chew-pid
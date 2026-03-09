class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)-1, -1, -1):
            if not stack:
                stack.append([temperatures[i], i])
                continue
            if stack[-1][0] > temperatures[i]:
                answer[i] = stack[-1][1] - i
                stack.append([temperatures[i], i])
                
            else:
                while stack and stack[-1][0] <= temperatures[i]:
                    stack.pop()
                if stack:
                    answer[i] = stack[-1][1] - i
                stack.append([temperatures[i], i])
        return answer



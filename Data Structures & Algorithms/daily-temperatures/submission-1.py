class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0 for _ in range(len(temperatures))]
        for i, num in enumerate(temperatures):
            while stack and stack[-1][0] < num:
                cur = stack.pop()
                output[cur[1]] = i - cur[1]
            stack.append([num,i])
        return output
                

            
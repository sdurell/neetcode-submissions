class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(temperatures))]
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                popI, popTemp = stack.pop()
                res[popI] = i - popI
            stack.append([i, temp])
        return res

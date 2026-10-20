class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)

        for i, num in enumerate(temperatures):
            while stack and stack[-1][0] < num:
                topNum, topI = stack.pop()
                output[topI] = i - topI # calculate how far ahead i is
            stack.append((num, i))
        return output

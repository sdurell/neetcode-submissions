'''

'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(temperatures))]
        distance = 0

        for i in range(0, len(temperatures)):
            while stack and stack[-1][1] < temperatures[i]:
                item = stack.pop()
                distance += 1
                res[item[0]] = i - item[0]
            stack.append((i, temperatures[i]))
            distance = 0
        
        return res
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [[position[i], speed[i]] for i in range(len(position))]
        time.sort(reverse=True, key = lambda x: x[0])
        time = [(target - pos) / spd for pos, spd in time]

        stack = []
        for t in time:
            stack.append(t)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
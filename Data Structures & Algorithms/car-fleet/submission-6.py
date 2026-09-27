class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]

        cars.sort()
        cars.reverse()
        stack = []
        for car in cars:
            stack.append((target - car[0]) / car[1])
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

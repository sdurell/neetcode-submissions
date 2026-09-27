'''
getMin must be O(1)

'''
class MinStack:

    def __init__(self):
        self.data = []
        self.minStack = []

    def push(self, val: int) -> None:
        if self.data:
            minP = min(self.minStack[-1], val)
            self.minStack.append(minP)
        else:
            self.minStack.append(val)
        self.data.append(val)

    def pop(self) -> None:
        self.minStack.pop()
        self.data.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

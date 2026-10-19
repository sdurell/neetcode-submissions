class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {')' : '(', ']': '[', '}': '{'}
        stack = []
        for bracket in s:
            if bracket in open_to_close:
                if stack and stack[-1] == open_to_close[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        return False if stack else True
class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {"(" : ")", "[" : "]", "{" : "}"}
        stack = []

        for char in s:
            if char in closeToOpen.keys():
                stack.append(char)
            else:
                if stack and closeToOpen.get(stack[-1]) == char:
                    stack.pop()
                else:
                    stack.append(char)
        return not stack
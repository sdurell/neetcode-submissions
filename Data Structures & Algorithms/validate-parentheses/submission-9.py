class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
            else:
                peek = stack[-1] if stack else None
                if char == ")" and peek == "(":
                    stack.pop()
                elif char == "}" and peek == "{":
                    stack.pop()
                elif char == "]" and peek == "[":
                    stack.pop()
                else:
                    stack.append(char)
        return not stack
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        lvalue, rvalue = 0, 0
        for char in tokens:
            if char in ["+", "*", "-", "/"]:
                rvalue = int(stack.pop())
                lvalue = int(stack.pop())
                if char == "+":    
                    lvalue = lvalue + rvalue
                elif char == "*":
                    lvalue = lvalue * rvalue
                elif char == "-":
                    lvalue = lvalue - rvalue
                else:
                    lvalue = lvalue / rvalue
                stack.append(lvalue)
            else:
                stack.append(char)
        return int(stack.pop())

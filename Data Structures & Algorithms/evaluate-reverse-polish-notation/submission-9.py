class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for elem in tokens:
            if elem in ["+", "-", "/", "*"]:
                y, x = stack.pop(), stack.pop()
                if elem == "+":
                    stack.append(x + y)
                elif elem == "-":
                    stack.append(x - y)
                elif elem == "/":
                    stack.append(int(x / y))
                elif elem == "*":
                    stack.append(x * y)
            else:
                stack.append(int(elem))
        return stack[-1]
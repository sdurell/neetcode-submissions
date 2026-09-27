'''

'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if len(stack) > 1 and char == '+':
                val = stack.pop()
                stack[-1] += val 
            elif len(stack) > 1 and char == '-':
                val = stack.pop()
                stack[-1] -= val
            elif len(stack) > 1 and char == '*':
                val = stack.pop()
                stack[-1] *= val
            elif len(stack) > 1 and char == '/':
                val = stack.pop()
                stack[-1] = int(stack[-1] / val)
            else:
                stack.append(int(char))
        
        return stack[0]
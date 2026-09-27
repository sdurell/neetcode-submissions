class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char_map = {'(': ')', '{': '}', '[': ']'}

        for char in s:
            if char in [')', '}', ']']:
                if not stack:
                    return False
                elif stack and char != char_map[stack.pop()]:
                    return False
            else:
                stack.append(char)
                
        if stack:
            return False
        return True
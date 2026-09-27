class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def promising(stack, numOpen, char):
            if numOpen > n:
                return False
            if not stack and char == ")":
                return False
            return True           

        def dfs(arr, stack, count, numOpen):
            popFlag = False
            if count >= n:
                res.append("".join(arr))
                return

            #backtracking
            if promising(stack, numOpen + 1, "("):
                arr.append("(")
                stack.append("(")
                dfs(arr, stack, count, numOpen + 1)
                arr.pop()
                stack.pop()
            
            if promising(stack, numOpen, ")"):
                arr.append(")")
                if stack:
                    stack.pop()
                    popFlag = True
                    count += 1
                dfs(arr, stack, count, numOpen)
                arr.pop()
                if popFlag:
                    stack.append("(")
                    count -= 1
        
        dfs([], [], 0, 0)
        return res



        
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxH = 0
        for i, h in enumerate(heights):
            length = i
            while stack and h < stack[-1][1]:
                cur = stack.pop()
                maxH = max(maxH, cur[1] * (i - cur[0]))
                length = cur[0]
            stack.append([length, h]) 

        for i, h in stack:
            maxH = max(maxH, h * (len(heights) - i))
        return maxH
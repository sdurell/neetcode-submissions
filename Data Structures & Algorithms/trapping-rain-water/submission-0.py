class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0 for _ in range(len(height))]
        postfix = [0 for _ in range(len(height))]
        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1:
                prefix[i] = 0
                continue
            postfix[i] = max(height[i+1], postfix[i+1])
        water = 0
        for i in range(len(height)):
            if i == 0:
                prefix[i] = 0
                continue
            prefix[i] = max(height[i-1], prefix[i-1])
            if min(prefix[i], postfix[i]) - height[i] > 0:
                water += min(prefix[i], postfix[i]) - height[i]
        return water


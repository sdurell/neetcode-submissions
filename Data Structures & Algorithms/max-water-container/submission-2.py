class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # notes
        # Maximize area: maximize width (r-l) and height (min(h[l], h[r]))
        # Which way should pointer go? Cant maximize width any more, so try to maximize height
        # How? Choose pointer that that points to the smaller height. Changing smaller height may
        # give a bigger height. 
        l, r = 0, len(heights) - 1

        maxH = float("-inf")
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            maxH = max(area, maxH)
            
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxH

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hMap = set()
        maxL = 0
        l = 0
        for r, char in enumerate(s):
            while s[r] in hMap:
                hMap.remove(s[l])
                l += 1
            hMap.add(s[r])
            length = r - l + 1
            maxL = max(maxL, length)
        return maxL

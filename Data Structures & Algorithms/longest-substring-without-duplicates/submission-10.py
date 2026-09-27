class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hmap = set()
        l = 0
        maxLen = 0
        for r in range(len(s)):
            while s[r] in hmap:
                hmap.remove(s[l])
                l += 1
            hmap.add(s[r])
            maxLen = max(maxLen, r - l + 1)
        return maxLen
